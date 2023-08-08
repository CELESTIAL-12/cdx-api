from django.urls import path
from . import views

urlpatterns = [
    path('question/',views.Question_output,name = 'question')
]
