from django.conf.urls import url

from .views import SurveyListCreate


urlpatterns = [
    url(r'^$', SurveyListCreate.as_view())
]
