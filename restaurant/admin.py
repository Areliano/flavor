from django.contrib import admin

# Register your models here.

#from . models import Homepage




from . models import Customer, Menu, Homepage, Restaurant, Aboutpage

admin.site.register(Customer)

admin.site.register(Menu)

admin.site.register(Homepage)

admin.site.register(Restaurant)

admin.site.register(Aboutpage)