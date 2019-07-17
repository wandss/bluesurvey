from django.conf.urls import url

from .views import QuestionListCreate

urlpatterns = [
    url(r'^questions', QuestionListCreate.as_view()),
]
