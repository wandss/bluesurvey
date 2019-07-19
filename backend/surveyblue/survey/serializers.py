from rest_framework.serializers import ModelSerializer, SerializerMethodField

from question.serializers import QuestionSerializer
from .models import Survey, Survey_Question



class SurveySerializer(ModelSerializer):

    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = '__all__'

    def create(self, validated_data):

        question_data = validated_data.pop('questions')
        survey = Survey.create(**validated_data)

        for question in question_data:
            # TODO CONTINUE FROM HERE
            # COMPLEX NESTED OBJECT.
            import pdb; pdb.set_trace()  #DEBUG


        return survey
