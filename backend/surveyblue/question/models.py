from django.db import models


class OptionResponse(models.Model):

    description = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.description


class Question(models.Model):
    # TODO: Overwrite save method
    # when QUESTION_TYPE is 3 or scale,
    # options must be provided

    QUESTION_TYPE = (
        (0, "Simple Input"),
        (1, "Multiline Input"),
        (2, "Unique Choice"),
        (3, "Mutiple Choice"),
        (4, "Scale")
    )

    description = models.CharField(max_length=500, unique=True)
    question_type = models.IntegerField(choices=QUESTION_TYPE)
    options = models.ManyToManyField(OptionResponse, blank=True)

    def __str__(self):
        return self.description
