from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class QuestionTypeChoice(models.IntegerChoices):
        TEXT = 1, 'Text'
        CHECKBOX = 2, 'Checkbox'
        RADIO_SELECT = 3, 'Radio'
        DROP_LIST = 4, 'Drop List'

    type_question = models.IntegerField(choices=QuestionTypeChoice.choices)


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField()
    bool_answer = models.BooleanField(default=False)


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)


