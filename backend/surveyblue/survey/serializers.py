from rest_framework.serializers import ModelSerializer

from question.models import Question
from question.serializers import QuestionSerializer
from .models import Survey, Survey_Question


class SurveySerializer(ModelSerializer):
    # TODO: Add field for layout
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = '__all__'

    def create(self, validated_data):

        validated_data.pop('questions')
        clients_data = validated_data.pop('clients', [])
        survey = Survey.objects.create(**validated_data)
        data = self.get_initial()
        questions = data.get('questions')

        for client in clients_data:
            survey.clients.add(client)

        for question in questions:
            question_instance = Question.objects.get(pk=question.get('id'))
            survey.survey_question_set.create(survey=survey,
                                              question=question_instance)

        return survey
