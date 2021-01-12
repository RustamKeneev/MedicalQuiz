from django.shortcuts import render
from django.views.generic.base import View
from .models import Quiz,Category

class QuizView(View):
    """Список опросников"""
    def get(self,request):
        quiz = Quiz.objects.all()
        return render(request,"quiz/quiz_list.html",{"quiz_list":quiz})

class CategoryView(View):
    """Список категорий"""
    def get(self,request):
        category = Category.objects.all()
        return render(request,"quiz/quiz_list.html",{"quiz_category_list":category})