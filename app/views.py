from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == "POST":
        # print(request.POST)
        quiz_id = request.POST.get('bookmark') #2
        quiz = Quiz.objects.get(id = quiz_id ) #react
        
        bookmark = Bookmark.objects.filter(quiz = quiz,user = request.user).first()

        if bookmark:
            bookmark.delete()
            messages.success(request,'Bookmarked removed')
            return redirect('/')
    
        Bookmark.objects.create(quiz =quiz,user = request.user)
        messages.success(request,'Bookmarked added')

        return redirect('/')


    quizes = Quiz.objects.all()

    return render(request,'index.html',{
        'quizes':quizes
    })



def quizview(request,id):
    try:
        quiz = Quiz.objects.get(id = id)
        questions = quiz.quizs.all()
        
        if request.method == "POST":
            for question in questions:
                question_id = str(question.id)
                selected_answer = request.POST.get(question_id)
                correct_answer  = Answers.objects.filter(question = question,is_correct = True ).first()
                if selected_answer == correct_answer.answer:
                    print("correct")
                    
                else:
                    print("wrong")
            return redirect('/')
            

                
        return render(request,'quizview.html',{
            "questions":questions
        })
    except:
        return render(request,'error.html')