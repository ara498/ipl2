from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain (request):
    return HttpResponse('<h1><marquee>hardik pandiya is an modern-day Indian cricketer</marquee></h1>')

