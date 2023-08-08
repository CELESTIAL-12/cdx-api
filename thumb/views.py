#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.http import HttpResponse,JsonResponse,HttpResponse
from django.views.generic import ListView,DetailView,TemplateView
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AnswerSerializer
from .models import Final
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
import json


# Movies = {"Movies1": "WAR", select_ip = "0.0.0.0:"+str(port)}

class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Final.objects.all()
    serializer_class = AnswerSerializer

    
    def list(self, request, *args, **kwargs):
        answer = Final.objects.all()
        serializer = AnswerSerializer(answer, many=True)    
        return Response(serializer.data)


@csrf_exempt
def Question_output(request):

    request_body = json.loads(request.body)
    en = Final(Question = request_body.get('Question'))
    en.save()
    
    print(en)
    strq = "Data inserted"
    print("gello")
    return render(request,'index.html', {"msg":strq})