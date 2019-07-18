from rest_framework.generics import ListCreateAPIView

from .models import OptionResponse, Question
from .serializers import OptionResponseSerializer, QuestionSerializer


class QuestionListCreate(ListCreateAPIView):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
