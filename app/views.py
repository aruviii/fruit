from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login , authenticate

from .models import CustomUser

from .forms import ProductsForm

from .models import Products

def index(request):

	context = {
	'title':"Store",
	'current_user':"Login Please",
	'products':Products.objects.all(),
	}
	
	return render(request,'app/index.html',context)

def register(request):
	form = RegistrationForm()
	context = {
	"form" : form,
	}
	if request.user.is_authenticated :
		context['current_user']=CustomUser.objects.get(email=request.user.email)

	return render(request,'app/register.html',context)

def login(request):
	context = {
	}
	return render(request,'app/login.html',context)

def admin(request):
	context = {
	'product_form':ProductsForm,
	'products':Products.objects.all(),
	}
	if request.method=='POST':
		form = ProductsForm(request.POST)
		if form.is_valid():
			form.save()
	
	return render(request,'app/admin.html',context)