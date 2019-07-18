from django.conf.urls import url

from .views import QuestionListCreate


urlpatterns = [
    url(r'^$', QuestionListCreate.as_view()),
]
