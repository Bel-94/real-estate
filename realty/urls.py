from django.urls import path
from django.conf.urls.static import static
from Estate import settings
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('', views.pages, name='index'),
    path('about', views.about, name='about')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
