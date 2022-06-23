from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
]
