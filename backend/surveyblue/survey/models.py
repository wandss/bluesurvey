from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from question.models import Question


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
    questions = models.ManyToManyField(Question)
    clientes = models.ManyToManyField(User)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
