# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def Products(request):
    return render(request, 'products/product1page.html')

