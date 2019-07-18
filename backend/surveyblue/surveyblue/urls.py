from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'api/v1/questions/', include('question.urls', namespace="questions")),
    url(r'api/v1/surveys/', include('survey.urls', namespace="survey")),
]
