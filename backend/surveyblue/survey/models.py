from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from question.models import Question, OptionResponse


class Survey(models.Model):

    STATUS = (
        (0, "Created"),
        (1, "In process"),
        (3, "Finished")
    )

    title = models.CharField(max_length=300, unique=True)
    objective = models.TextField(blank=True, null=True)
    begin_date = models.DateField()
    end_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name="author")
    status = models.IntegerField(choices=STATUS)
    questions = models.ManyToManyField(Question, through='Survey_Question',
                                       blank=True)
    clients = models.ManyToManyField(User)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Survey_Question(models.Model):
    LAYOUT = (
        (0, "Vertical"),
        (1, "Horizontal"),
    )

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    layout = models.IntegerField(choices=LAYOUT)


class Answer(models.Model):

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    multiple_choice = models.ForeignKey(OptionResponse, null=True,
                                        blank=True, on_delete=models.CASCADE)
    explanation = models.TextField(blank=True, null=True)
    date_answer = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['client', 'survey', 'question']

    def __str__(self):
        return "{}-{}-{}".format(self.survey, self.question, self.client)
