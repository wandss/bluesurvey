from django.conf.urls import url

from .views import SurveyListCreate, SurveyUpdate


urlpatterns = [
    url(r'^$', SurveyListCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/update$', SurveyUpdate.as_view()),
]
