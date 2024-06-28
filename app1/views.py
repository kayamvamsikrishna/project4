from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def httpRes(request):
    return HttpResponse('httpResponse is done guru') 