from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .serializers import QuizSerializer
from .views import QuestionListView, OptionListViewSet,OptionViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import url,include

router = SimpleRouter()
router.register("options", OptionViewSet, "options")
router.register("optionslist",OptionListViewSet,"optionslist")


urlpatterns = [
    path("",views.QuizView.as_view()),
    path('api/quiz/', views.get_all_quizs),
    path('api/quiz/<int:id>/', views.get_options),
    path('api/quiz/questions/', QuestionListView.as_view(),name='question_list'),
    path('api/quiz/questions/<int:id>', QuestionListView.as_view(),name='question_detail'),
    path('api/quiz/', include(router.urls)),
    path('api/quiz/',include(router.urls)),
]
