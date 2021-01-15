from django.shortcuts import render
from django.views.generic.base import View
from .models import Quiz,Category,Option

class QuizView(View):
    """Список опросников"""
    def get(self,request):
        quiz = Quiz.objects.all()
        return render(request,"quiz/quiz_list.html",{"quiz_list":quiz})


def checklist(request,id):
    if request.method == "POST":
        pass


# class CategoryView(View):
#     """Список категорий"""
#     def get(self,request):
#         category = Category.objects.all()
#         return render(request,"quiz/quiz_list.html",{"quiz_category_list":category})
#
# class OptionView(View):
#     """Список чексбоксов"""
#     def get(self,request):
#         options = Option.objects.all()
#         return render(request,"quiz/quiz_list.html",{"quiz_option_list":options})