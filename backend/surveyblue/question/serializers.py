from rest_framework.serializers import ModelSerializer

from .models import OptionResponse, Question, Question_OptionResponse


class OptionResponseSerializer(ModelSerializer):

    class Meta:
        model = OptionResponse
        fields = '__all__'


class QuestionSerializer(ModelSerializer):

    options = OptionResponseSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


    def create(self, validated_data):

        options_data = validated_data.pop('options', [])
        question = Question.objects.create(**validated_data)

        for options in options_data:
            option = OptionResponse.objects.create(**options)
            question_option = Question_OptionResponse.objects.create(
                question=question, option_response=option)
            question.question_optionresponse_set.add(question_option)


        return question
