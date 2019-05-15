from collections import OrderedDict
from api.serializers import (
    SurveyCompanyNameSerializer,
    SurveySerializer,
    SurveyWithResultSerializer,
)
from core.models import Survey, SurveyResult
from django.conf import settings
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    get_object_or_404,
    ListAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from core import aggregate
from core.conf.utils import flatten
from rest_framework import status


class CreateSurveyView(CreateAPIView):
    """
    Internal API endpoint to create a survey and return the created survey data including both link and link_sponsor.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()


class SurveyCompanyNameFromUIDView(RetrieveAPIView):
    """
    External API endpoint to get the company name given a UID.
    Must use `sid` GET param to specify company: e.g. ?sid=a95c7b47c8e2e1d057c56d114bb2862c
    """
    # Only allow authentication via token
    # Only using session authentication by default everywhere else
    # locks out anyone with a token from using any of the other endpoints
    authentication_classes = (TokenAuthentication,)
    serializer_class = SurveyCompanyNameSerializer
    queryset = Survey.objects.all()
    lookup_field = 'sid'
    lookup_url_kwarg = 'sid'
    _bypass_domain_restriction = True

    def retrieve(self, request, *args, **kwargs):
        """
        Overridden RetrieveAPIView retrieve() to get instance via GET param instead of URL keyword arg.
        """
        instance = get_object_or_404(self.queryset, **{self.lookup_field: request.GET.get(self.lookup_url_kwarg)})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SurveyDetailView(RetrieveAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SurveyWithResultSerializer
    queryset = Survey.objects.all()
    lookup_field = 'sid'
    lookup_url_kwarg = 'sid'

    def retrieve(self, request, sid, *args, **kwargs):
        """
        Overridden RetrieveAPIView retrieve() to get instance via GET param instead of URL keyword arg.
        """
        survey_instance = get_object_or_404(self.queryset, **{self.lookup_field: sid})
        survey_instance.survey_result = survey_instance.last_survey_result
        serializer = self.get_serializer(survey_instance)
        return Response(serializer.data)


class SurveyResultDetailView(RetrieveAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SurveyWithResultSerializer
    queryset = SurveyResult.objects.all()
    lookup_field = 'response_id'
    lookup_url_kwarg = 'response_id'

    def retrieve(self, request, response_id, *args, **kwargs):
        """
        Overridden RetrieveAPIView retrieve() to get instance via GET param instead of URL keyword arg.
        """
        survey_result_instance = get_object_or_404(self.queryset, **{self.lookup_field: response_id})
        survey_instance = survey_result_instance.survey
        if not survey_instance:
            raise Http404
        survey_instance.survey_result = survey_result_instance
        serializer = self.get_serializer(survey_instance)
        return Response(serializer.data)


class SurveyResultsIndustryDetail(APIView):
    """
    Returns the bechmark data given an industry.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, industry, *args, **kwargs):

        tenant = self.request.query_params.get('tenant', None)

        if not tenant or tenant not in settings.TENANTS.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        industry_map = OrderedDict(flatten(settings.HIERARCHICAL_INDUSTRIES, leaf_only=False))
        if industry not in settings.INDUSTRIES.keys():
            return Response(status=status.HTTP_404_NOT_FOUND)

        dmb, dmb_d, dmb_industry = aggregate.industry_benchmark(tenant, industry)
        dmb_bp, dmb_d_bp, dmb_bp_industry = aggregate.industry_best_practice(tenant, industry)

        data = {
            'industry': industry_map[industry],
            'dmb_industry': industry_map.get(dmb_industry, settings.ALL_INDUSTRIES[0]),
            'dmb_bp_industry': industry_map.get(dmb_bp_industry, settings.ALL_INDUSTRIES[0]),
            'dmb': dmb,
            'dmb_d': dmb_d,
            'dmb_bp': dmb_bp,
            'dmb_d_bp': dmb_d_bp,
        }
        return Response(data)


class AdminSurveyListView(ListAPIView):
    authentication_classes = (SessionAuthentication,)
    serializer_class = SurveyWithResultSerializer

    def get_queryset(self):
        """
            Return a list of all the surveys that the authenticated
            user has ever sponsored, filtered by `tenant`.
        """
        tenant = self.kwargs['tenant']
        user = self.request.user
        queryset = Survey.objects.filter(tenant=tenant)
        if not user.is_super_admin:
            queryset = queryset.filter(engagement_lead=user.engagement_lead)
        return queryset
