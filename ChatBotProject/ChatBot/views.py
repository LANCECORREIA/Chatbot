import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .chatbot import get_response, predict_class

# Create your views here.


@csrf_exempt
@api_view(["POST"])
def predict(request):
    message = request.data.get("message")
    intents = json.loads(open("../model/intents.json").read())
    intent = predict_class(message)
    response = get_response(intent,intents)
    return JsonResponse({"answer": response})
