from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True)

    def __str__(self):
        return self.title

class Questions(models.Model): 
    question = models.CharField(max_length = 200 )
    quiz = models.ForeignKey(Quiz,on_delete = models.CASCADE,related_name = "quizs")
    def __str__(self):
        return self.question

class Answers(models.Model):
    answer = models.CharField(max_length = 100)
    question = models.ForeignKey(Questions,on_delete = models.CASCADE,related_name = "questions")
    is_correct = models.BooleanField(default = False)

    def __str__(self):
        return self.answer

