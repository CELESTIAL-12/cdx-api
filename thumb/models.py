from django.db import models

# Create your models here.
class Final(models.Model):
    
    # question = models.CharField(max_length = 500)
    answer = models.CharField(max_length=10000)
    Question = models.CharField(max_length = 500)

# class Question(models.Model):