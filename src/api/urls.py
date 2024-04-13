from rest_framework import routers

from .views import QuestionAnswerViewSet, QuestionViewSet, QuizViewSet, UserAnswerViewSet

router = routers.DefaultRouter()
router.register(r'quizzes', QuizViewSet)

router.register(r'questions', QuestionViewSet)

router.register(r'question-answers', QuestionAnswerViewSet)

router.register(r'user-answers', UserAnswerViewSet)

urlpatterns = []
urlpatterns += router.urls

