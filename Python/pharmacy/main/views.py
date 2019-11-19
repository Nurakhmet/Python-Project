from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Catalogue, Order, Account

# Create your views here.

def index(response, id):
	user = User.objects.get(id = id)
	return render(response, "main/user.html", {"user":user})

def home(response):
	return render(response, "main/home.html", {})

def buy(response):
	return render(response, "main/buy.html", {})

#admin username = nomad
#password = 123
