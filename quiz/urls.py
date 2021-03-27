from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .serializers import QuizSerializer
from .views import QuestionListView, OptionListViewSet,OptionViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import url,include

urlpatterns = [
    path("",views.QuizView.as_view()),
    path('api/quiz/', views.get_all_quizs),
    path('api/quiz/<int:id>/', views.get_options),
    path('api/quiz/questions/', QuestionListView.as_view(),name='question_list'),
    path('api/quiz/questions/<int:id>', QuestionListView.as_view(),name='question_detail'),
    path('api/quiz/options/',OptionViewSet.as_view),
    path('api/quiz/optionslist/',OptionListViewSet.as_view),

]
