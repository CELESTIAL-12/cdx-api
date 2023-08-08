from django.shortcuts import render
# from llm import generate_response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chat.final_vicuna import load_model, generate_text
import json

@csrf_exempt

def generate_response(request):
    
#    tokenizer, model = load_model()
    request_body = json.loads(request.body)
    question = request_body.get('Question')
    
    response = generate_text(question)
    # prompt = request.GET.get('prompt', '')
    # response = f'LLM generated response for: "{pr}"'
    return JsonResponse(request,{'response': response})
