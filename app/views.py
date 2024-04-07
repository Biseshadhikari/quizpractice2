from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def home(request):
    if request.method == "POST":
        # print(request.POST)
        quiz_id = request.POST.get('bookmark') #2
        quiz = Quiz.objects.get(id = quiz_id ) #react
        
        bookmark = Bookmark.objects.filter(quiz = quiz,user = request.user).first()

        if bookmark:
            bookmark.delete()
            return redirect('/')
    
        Bookmark.objects.create(quiz =quiz,user = request.user )
        

        
        return redirect('/')


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