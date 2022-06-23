from django.contrib import admin
from .models import Realtor, Contacts, Listing

# Register your models here.
# This class is not necessary but I had to write and see if there is a difference anyway
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','listing','email','contact_date')
    list_display_link=('id','name')
    search_fields=('name','email','listing')
    list_per_page=25
admin.site.register(Contacts, ContactAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'name')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('name', 'description', 'address',
                     'location', 'county', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
