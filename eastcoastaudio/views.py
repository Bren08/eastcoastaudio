from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("<h1 style='text-align: center;'>Welcome to our new shop EastCoastAudio</h1>")