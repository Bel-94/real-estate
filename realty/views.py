from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

# imports for creating authentication
from django.contrib.auth.models import User
from .models import Contacts

# Create your views here.

#function for the home page
@login_required(login_url='login')
def index(request):
    return HttpResponse('Welcome to your dream home')


