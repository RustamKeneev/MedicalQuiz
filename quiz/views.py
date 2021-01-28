from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Quiz,Category,Option
from .serializers import QuizSerializer


class QuizView(View):
    """Список опросников"""
    def get(self,request):
        quiz = Quiz.objects.all()
        return render(request,"quiz/quiz_list.html",{"quiz_list":quiz})


def checklist(request,id):
    if request.method == "POST":
        pass

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

