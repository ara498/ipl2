from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain (request):
    return HttpResponse('<h1><marquee>msd is great indian wicketkeeper</marquee></h1>')