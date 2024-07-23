# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *

def AuthPage(request):
	return render(request, 'auth/AuthPage.html')
	
def CompanyRegistration(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password2')
		user = Customer.objects.filter(username=username)
		if user.exists():
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		post_data = request.POST.copy()  # Make a mutable copy of POST data
		post_data['category'] = 'C'  # Set the category to 'Company'
		CustomerForm = CompanyRegistrationForm(data=post_data)
		if CustomerForm.is_valid():
			CustomerForm.save()
			created_user = Customer.objects.get(username=CustomerForm.data['username'])
			created_user.set_password(password)
			created_user.save()
			messages.info(request, "Account created Successfully!")
		else:
			messages.error(request, CustomerForm.errors)
			return redirect('CompanyRegistrationView')
	return render(request, 'auth/CompanyRegistration.html')

def AuthLogin(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		if not Customer.objects.filter(username=username).exists():
			messages.error(request, 'Invalid Username')
			return redirect('AuthLoginView')
		user = authenticate(username=username, password=password)
		if user is None:
			messages.error(request, "Invalid Password")
			return redirect('AuthLoginView')
		else:
			login(request, user)
			return render(request, 'pages/home.html')
	return render(request, 'auth/login.html')