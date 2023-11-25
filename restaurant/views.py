from django.shortcuts import render, redirect

from .models import Restaurant, Customer, Aboutpage

from django.http import HttpResponse

#from restaurant.models import Homepage


# Create your views

def index(request):
    link = Restaurant.objects.all()
    #slides =  Homepage.objects.all()[5000]
    return render(request, 'index.html', {"link": "index"})


def about(request):
    information = Aboutpage.objects.all
    return render(request, "about.html", {"link": "about", "rest":information})


def blog(request):
    return render(request, "blog.html", {"link": "blog"})


# def blog-single(request):
#  return render(request, "blog-single.html", {"link":"blog-single"})


def contact(request):
    return render(request, "contact.html", {"link": "contact"})


# def index(request):
#     return render(request, "index.html", {"link":"index"})


def menu(request):
    return render(request, "menu.html", {"link": "menu"})


def reservation(request):
    return render(request, "reservation.html", {"link": "reservation"})

def booked(request):
    customers = Customer.objects.all()
    return render(request, "booked.html", {"link":"booked", "data":customers})

def dropdown(request):
    return render(request, "dropdown.html", {"link":"dropdown"})

def delete(request, id):
    satisfied_customer = Customer.objects.get(id=id)

    satisfied_customer.delete()

    return render(request, 'booked.html')







    return render(request, 'booked.html')