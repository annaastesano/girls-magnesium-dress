from djangae.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import override_settings

from core.test import with_appengine_admin, with_appengine_user
from core.tests.mommy_recepies import make_survey, make_survey_result
from core.tests import mocks
from django.conf import settings
import os
from core.test import reload_urlconf, TempTemplateFolder


@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    ALLOWED_TENANTS=mocks.MOCKED_ALLOWED_TENANTS,
    TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
    DEFAULT_TENANT='tenant1',
)
class ReportsAdminTestCase(TestCase):
    """Tests for `reports_admin` view."""

    @classmethod
    def tearDownClass(cls):
        super(ReportsAdminTestCase, cls).tearDownClass()
        reload_urlconf()

    @classmethod
    def setUpClass(cls):
        super(ReportsAdminTestCase, cls).setUpClass()
        reload_urlconf()

    def setUp(self):
        self.url = reverse('reports', kwargs={'tenant': 'tenant1-slug'})
        self.survey_1 = make_survey()
        self.survey_2 = make_survey()

        self.survey_result_1 = make_survey_result(
            survey=self.survey_1,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )

        self.survey_result_2 = make_survey_result(
            survey=self.survey_2,
            response_id='BBB',
            dmb=1.0,
            dmb_d='{}'
        )

    @with_appengine_user('test@google.com')
    def test_standard_user_logged_in(self):
        """Standard user can retrieve reports belonging to its engagement_lead."""

        self.user = get_user_model().objects.create(email='test@google.com')

        # set a survey to belong to logged user
        self.survey_1.engagement_lead = self.user.engagement_lead
        self.survey_1.save()

        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant1')
        with TempTemplateFolder(templates_path, 'reports-list.html'):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            surveys = list(response.context.get('surveys'))

            self.assertTrue(surveys)
            self.assertEqual(len(surveys), 1)
            self.assertEqual(surveys[0].engagement_lead, self.survey_1.engagement_lead)

    @with_appengine_admin('test@google.com')
    def test_whitelisted_user_logged_in(self):
        """Whitelisted user can retrieve reports belonging to all companies."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant1')
        with TempTemplateFolder(templates_path, 'reports-list.html'):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            surveys = list(response.context.get('surveys'))
            engagement_lead_ids = [el.engagement_lead for el in surveys]

            self.assertTrue(surveys)
            self.assertEqual(len(surveys), 2)
            self.assertTrue(self.survey_1.engagement_lead in engagement_lead_ids)
            self.assertTrue(self.survey_2.engagement_lead in engagement_lead_ids)

    def test_user_not_logged_in(self):
        """Anonymous user cannot retrieve any report."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(reverse('djangae_login_redirect') in response.get('Location'))

    @with_appengine_user('notenoughpermissions@gmail.com')
    def test_user_logged_in_not_in_permission_domains(self):
        """User could be logged in, but not having enough permissions to access to the resource."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)


@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    ALLOWED_TENANTS=mocks.MOCKED_ALLOWED_TENANTS,
    TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
)
class ReportDetailTestCase(TestCase):
    """Tests for `report_static` view."""

    def setUp(self):
        reload_urlconf()
        self.tenant_slug = 'tenant1-slug'
        self.survey_1 = make_survey()
        self.survey_2 = make_survey()

        self.survey_result_1 = make_survey_result(
            survey=self.survey_1,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )
        self.survey_1.last_survey_result = self.survey_result_1
        self.survey_1.save()

    def test_survey_has_survey_result(self):
        """If a a`Survey` exists and it has a result, it should return 200."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant1')
        with TempTemplateFolder(templates_path, 'report-static.html'):
            url = reverse('report', kwargs={'tenant': self.tenant_slug, 'sid': self.survey_1.sid})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_survey_does_not_exist(self):
        """If a a`Survey` does not exists it should raise 404."""
        with override_settings(
            TENANTS=mocks.MOCKED_TENANTS,
            ALLOWED_TENANTS=mocks.MOCKED_ALLOWED_TENANTS,
            TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
        ):

            url = reverse('report', kwargs={'tenant': self.tenant_slug, 'sid': '12345678890'})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

    def test_survey_does_not_have_a_result(self):
        """If a a`Survey` exists, but doesn't have a result, it should raise 404."""
        url = reverse('report', kwargs={'tenant': self.tenant_slug, 'sid': self.survey_2.sid})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
