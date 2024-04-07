from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name = "home"),
    path('quizview/<int:id>/',quizview,name = "quizview")
]
