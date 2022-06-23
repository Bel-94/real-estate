from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

# imports for creating authentication
from django.contrib.auth.models import User
from .models import Contacts, Listing
from django.contrib import messages, auth

# imports for creating the view functions for the project
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.

# function for registration form
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match 
        if password==password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request,'registration/register.html')


# function for log in
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'registration/login.html')


# function for logout
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')


# function for user dashboard
def dashboard(request):
    user_contacts= Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context ={
        'contacts':user_contacts
    }
    return render(request,'registration/dashboard.html',context)

#function for the home page

def index(request):
    listings = Listing.objects.order_by('-list_data').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'main/listings.html', context)

# function for getting the listings
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing':listing
    }

    return render(request, 'main/listing.html', context)

# function for search



