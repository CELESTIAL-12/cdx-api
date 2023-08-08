from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import question
import json
#from .serializers import QuestionSerializer

# Create your views here.
@csrf_exempt
def Question_output(request):
    
    request_body = json.loads(request.body)
    en = question(Question = request_body.get('Question'))
    en.save()
    print(en)
    strq = "Data inserted"
    print("gello")
    return render(request,'index.html', {"msg":strq})