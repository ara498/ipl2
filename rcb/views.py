from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain (request):
    return HttpResponse('<h1><marquee>virat kohli is the best indian batsman</marquee></h1>')
