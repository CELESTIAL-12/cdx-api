from django.urls import path
from chat.views import generate_response
from .import views

urlpatterns = [
    path('generate/', views.generate_response, name='generate_response'),
]