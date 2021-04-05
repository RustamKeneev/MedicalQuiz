from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Quiz,Category,Option,OptionList
from .serializers import QuizSerializer, QuestionListSerializer,OptionSerializer,OptionMTMSerializer


class QuizView(View):
    """Список опросников"""
    def get(self,request):
        quiz = Quiz.objects.all()
        return render(request,"quiz/quiz_list.html",{"quiz_list":quiz})

#
# def checklist(request,id):
#     if request.method == "POST":
#         pass

@api_view(['GET'])
def get_all_quizs(request):
    quiz = Quiz.objects.all()
    data = QuizSerializer(quiz,many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_options(request,id):
    try:
        posts = Option.objects.get(id=id)
    except Quiz.DoesNotExist:
        return Response(data={'result': 'сообщение не существует'}, status=status.HTTP_404_NOT_FOUND)
    data = QuizSerializer(posts).data
    return Response(data=data, status=status.HTTP_200_OK)


class QuestionListView(generics.ListCreateAPIView):
    """Список вопросов"""
    serializer_class = OptionSerializer
    queryset = Option.objects.all()
    lookup_field = 'id'


class OptionViewSet(viewsets.ModelViewSet):
    serializer_class = OptionSerializer

    def get_queryset(self):
        options = Option.objects.all()
        return options

class OptionListViewSet(viewsets.ModelViewSet):
    serializer_class = OptionMTMSerializer
    queryset = OptionList.objects.all()
    def get_queryset(self):
        id = self.request.data["id"]
        option_list = OptionList.objects.filter(options__in=[id])
        return option_list


class OptionAPIView(generics.GenericAPIView):
    serializer_class = OptionMTMSerializer

    def post(self, request, *args, **kwargs):
        option_ids = request.data.get('ids')
        optionlists = (
            OptionList.objects
            .annotate(options__count=Count('options'))
            .filter(options__count=len(option_ids))
        )
        for option_id in option_ids:
            optionlists = optionlists.filter(options__id=option_id)
        serializer = self.serializer_class(optionlists, many=True)
        return Response(serializer.data)
