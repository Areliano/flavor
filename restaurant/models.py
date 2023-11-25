from django.db import models

# Create your models here.

class Homepage(models.Model):
    heading = models.CharField(max_length=500)
    description = models.TextField(max_length=3000, default='description')
    btn = models.CharField(max_length=20)
    image = models.ImageField(upload_to='homepage', default='homepage.jpg')

    def __str__(self):
        return self.heading

class Customer(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    person = models.IntegerField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)


class Aboutpage(models.Model):
    about = models.CharField(max_length=50)
    heading = models.CharField(max_length=150)
    description = models.TextField(max_length=4500, default='description of the restaurant')
