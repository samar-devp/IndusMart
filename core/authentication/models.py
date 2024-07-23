from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


def validate_gst_number(value):
    """
    Validate GST number format (Indian GST number format is used here).
    GST number is a 15-digit alphanumeric code.
    """
    gst_pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$')
    if not gst_pattern.match(value):
        raise ValidationError('%(value)s is not a valid GST number', params={'value': value})

class Customer(AbstractUser):
    CATEGORY_CHOICES = (
        ('I', 'Individual'),
        ('C', 'Company'),
    )
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    gst_number = models.CharField(max_length=255, blank=True, null=True, validators=[validate_gst_number])
    registration_number = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='I')