from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Survey
from .serializers import SurveySerializer


class SurveyListCreate(ListCreateAPIView):

    serializer_class = SurveySerializer
    queryset = Survey.objects.all()


class SurveyUpdate(RetrieveUpdateAPIView):

    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
