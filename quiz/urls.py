from django.urls import path
from .import views
from .serializers import QuizSerializer

urlpatterns = [
    path("",views.QuizView.as_view()),
    path('api/quiz/', views.get_all_quizs),
    path('api/quiz/<int:id>/', views.get_options),
    # path("category/",views.CategoryView.as_view()),
]