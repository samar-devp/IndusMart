from celery import shared_task
from django.utils import timezone
import random
from datetime import timedelta
from .models import OTP
from utils.auth import *

@shared_task
def generate_and_send_otp(email):
    otp = f"{random.randint(1000, 9999)}"  # Generate a 6-digit OTP
    print(otp, "________________otp")
    expires_at = timezone.now() + timedelta(minutes=10)  # OTP validity duration
    OTP.objects.create(email=email, otp=otp, expires_at=expires_at)
    send_otp(email, otp)
