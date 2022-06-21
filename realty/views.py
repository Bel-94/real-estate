from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404

# Create your views here.

#function for the home page
def index(request):
    return redirect(request, 'main/index.html')


