from django.shortcuts import render
from elsys.processors.api_processor import ApiTuesProcessor
# Create your views here.
PI = 3.14

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars(request):
    return render(request, 'cars.html')

def longest_comment(request):
    return JsonResponse(ApiProcessor.longest_comment(), safe=False)

def post_with_longest_title(request):
    return JsonResponse(ApiProcessor.post_with_longest_title(), safe=False)

def get_data(request):
    return JsonResponse(ApiTuesProcessor.get_data(), safe=False)

def get_min(request):
    return JsonResponse(ApiTuesProcessor.min_temp(), safe=False)

def get_max(request):
    return JsonResponse(ApiTuesProcessor.max_temp(), safe=False)

def get_avg(request):
    return JsonResponse(ApiTuesProcessor.avg_temp(), safe=False)
