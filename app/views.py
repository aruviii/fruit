from django.shortcuts import render, redirect
from .forms import RegistrationForm
# Create your views here.
from django.contrib.auth import login , authenticate

def index(request):
	context = {
	'name':"aravinth"
	}
	return render(request,'app/index.html',context)

def register(request):
	form = RegistrationForm()
	context = {
	"form" : form,
	}
	if request.method == "POST":
		print(request.POST)
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			print(email, raw_password)
			account = authenticate(email = email, password = raw_password )
			return redirect("index")
	return render(request,'app/register.html',context)

def login(request):
	context = {
	}
	return render(request,'app/login.html',context)