from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'smartcode/index.html')

def message(request):
    return render(request, 'smartcode/message.html')