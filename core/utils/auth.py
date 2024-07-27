from django.core.mail import send_mail
from django.conf import settings

def send_otp(email, otp):
    subject = 'Your OTP Code'
    message = f'Your OTP code is {otp}. It expires in 10 minutes.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)