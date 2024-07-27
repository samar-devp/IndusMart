# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import re
import random
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
from utils.auth import *
from .models import *
from .forms import *
from .tasks import *

def AuthPage(request):
    print(request.user, "111111111111111")
    return render(request, 'auth/auth.html')


@require_POST
def request_otp(request):
    form = OTPForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        generate_and_send_otp.delay(email)  # Call the Celery task asynchronously
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': {'user_data': ['Invalid email']}})


@csrf_exempt  # Use this decorator if you handle CSRF tokens manually or have them in your AJAX setup
@require_POST
def user_login(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        email_arr = request.POST.getlist('email', 'null')
        otp_arr = request.POST.getlist('otp', 'null')
        email = email_arr[0] if email_arr else None
        otp = otp_arr[0] if otp_arr else None
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, email):
            user = User.objects.filter(email=email).first()
        else:
            return JsonResponse({'success': False, 'errors': {'error': ['Invalid email']}})
        if user:
            otp_obj = OTP.objects.filter(email=email, otp=otp)
            if not otp_obj:
                return JsonResponse({'success': False, 'errors': {'error': ['Incorrect OTP']}})
            user = authenticate(request, email=user.email)
            if user is not None:
                login(request, user, backend='authentication.backends.PasswordlessAuthBackend')
                return JsonResponse({'success': True, 'redirect': '/product/home/'})
            else:
                return JsonResponse({'success': False, 'errors': {'error': ['Authentication failed']}})
        else:
            email_arr = request.POST.getlist('email', 'null')
            email = email_arr[0] if email_arr else None
            data = request.POST.copy()
            data['email'] = email
            form = UserForm(data)
            if form.is_valid():
                user = form.save()
                user = authenticate(request, email=user.email)  
                if user is not None:
                    login(request, user, backend='authentication.backends.PasswordlessAuthBackend')
                    return JsonResponse({'success': True, 'redirect': '/product/home/'})
                else:
                    return JsonResponse({'success': False, 'errors': {'error': ['Authentication failed']}})
            else:
                errors = form.errors.get_json_data()
                return JsonResponse({'success': False, 'errors': errors})
    return JsonResponse({'success': False, 'error': ['Invalid request.']})