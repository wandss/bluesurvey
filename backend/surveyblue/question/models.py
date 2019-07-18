from django.db import models


class OptionResponse(models.Model):

    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Question(models.Model):

    QUESTION_TYPE = (
        (0, "Simple Input"),
        (1, "Multiline Input"),
        (2, "Unique Choice"),
        (3, "Mutiple Choice"),
        (4, "Scale")
    )

    description = models.CharField(max_length=500)
    question_type = models.IntegerField(choices=QUESTION_TYPE)
    options = models.ManyToManyField(OptionResponse, related_name="option",
                                     through='Question_OptionResponse')

    def __str__(self):
        return self.description


class Question_OptionResponse(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_response = models.ForeignKey(OptionResponse,
                                        on_delete=models.CASCADE)

    class Meta:
        unique_together = ['question', 'option_response']
