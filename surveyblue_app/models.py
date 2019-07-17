import uuid
from django.db import models
from django.utils import timezone


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
    options = models.ManyToManyField(OptionResponse,
                                     through='Question_OptionResponse')

    def __str__(self):
        return self.description


class Survey(models.Model):

    STATUS = (
        (0, "Created"),
        (1, "In process"),
        (3, "Finished")
    )

    title = models.CharField(max_length=300)
    objective = models.TextField(blank=True, null=True)
    begin_date = models.DateField()
    end_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS)
    questions = models.ManyToManyField(Question,
                                     through='Survey_Question')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Client(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    surveys = models.ManyToManyField(Survey,
                                     through='Client_Survey')


    def __str__(self):
        return self.name


class Question_OptionResponse(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_response = models.ForeignKey(OptionResponse,
                                        on_delete=models.CASCADE)


class Survey_Question(models.Model):

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Client_Survey(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class Answer(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_response = models.ForeignKey(OptionResponse, on_delete=models.CASCADE)
    justificativa = models.TextField(blank=True, null=True)
