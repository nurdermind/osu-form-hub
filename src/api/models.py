from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)

    class QuestionTypeChoice(models.IntegerChoices):
        TEXT = 1, 'Text'
        CHECKBOX = 2, 'Checkbox'
        RADIO_SELECT = 3, 'Radio'
        DROP_LIST = 4, 'Drop List'

    type_question = models.IntegerField(choices=QuestionTypeChoice.choices)

    class Meta:
        ordering = ['quiz', 'position']

    def __str__(self):
        return self.quiz.title + " - " + self.get_type_question_display()


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return str(self.question) + " - " + self.answer


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)

    @property
    def answer(self):
        return self.question_answer.answer
