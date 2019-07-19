from rest_framework.serializers import ModelSerializer

from .models import OptionResponse, Question


class OptionResponseSerializer(ModelSerializer):

    class Meta:
        model = OptionResponse
        fields = '__all__'

    def validate(self, data):
        import pdb;pdb.set_trace()#DEBUG


class QuestionSerializer(ModelSerializer):

    options = OptionResponseSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'



    def create(self, validated_data):

        options_data = validated_data.pop('options')
        question = Question.objects.create(**validated_data)

        for option in options_data:
            option['description'] = option['description'].capitalize().strip()
            option_instance = OptionResponse.objects.create(**option)
            question.options.add(option_instance)

        return question
