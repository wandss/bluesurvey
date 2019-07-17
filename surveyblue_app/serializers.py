from rest_framework.serializers import ModelSerializer

from .models import (Question, Question_OptionResponse)

class QuestionOptionResPonseSerializer(ModelSerializer):

    class Meta:
        model = Question_OptionResponse
        fields = '__all__'


class QuestionSerializer(ModelSerializer):

    options = QuestionOptionResPonseSerializer(many=True)


    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):

        options_data = validated_data.pop('options')
        question = Question.objects.create(**validated_data)

        for option in options_data:
            Question_OptionResponse.create(question=question, **options_data)

        return question
