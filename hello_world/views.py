from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import time

def homePageView(request):
    '''Respond to an HTTP request with a simple web page.'''


    return HttpResponse('Hello, world')
