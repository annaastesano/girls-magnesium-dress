"""Recipies for the Survey models."""
from model_mommy import mommy


def make_survey(**kwargs):
    survey = mommy.make('core.Survey', **kwargs)
    sid = kwargs.get('sid')
    if sid:
        survey.sid = sid
        survey.save()
    return survey


def make_survey_result(**kwargs):
    return mommy.make('core.SurveyResult', **kwargs)