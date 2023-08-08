from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Final


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Final
        fields = ('id','answer')


