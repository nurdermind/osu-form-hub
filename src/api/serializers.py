from rest_framework import serializers

from .models import Question, QuestionAnswer, Quiz, UserAnswer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class UserAnswerSerializer(serializers.ModelSerializer):
    answer = serializers.ReadOnlyField()

    class Meta:
        model = UserAnswer
        fields = '__all__'
        read_only_fields = ('user',)
