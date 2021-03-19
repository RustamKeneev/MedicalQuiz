from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .serializers import QuizSerializer
from .views import QuestionListView

urlpatterns = [
    path("",views.QuizView.as_view()),
    path('api/quiz/', views.get_all_quizs),
    path('api/quiz/<int:id>/', views.get_options),
    path('api/quiz/questions/', QuestionListView.as_view(),name='question_detail'),
]
