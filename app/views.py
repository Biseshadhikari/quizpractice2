from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    quizes = Quiz.objects.all()
    return render(request,'index.html',{
        'quizes':quizes
    })



def quizview(request,id):
    try:
        quiz = Quiz.objects.get(id = id) #django
        questions = quiz.quizs.all()
        
        if request.method == "POST":
            print(request.POST)
        
        

        return render(request,'quizview.html',{
            "questions":questions
        })
    except:
        return render(request,'error.html')