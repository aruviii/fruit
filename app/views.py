from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login , authenticate

from .models import CustomUser

def index(request):
	context = {
	'current_user':CustomUser.objects.get(email = request.user.email )
	}
	print(context['current_user'].email)
	return render(request,'app/index.html',context)

def register(request):
	form = RegistrationForm()
	context = {
	"form" : form,
	}
	return render(request,'app/register.html',context)

def login(request):
	context = {
	}
	return render(request,'app/login.html',context)
