from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer

class CustomerAdmin(UserAdmin):
    # Define the fields to be used in displaying the Customer model.
    # These fields are displayed on the list page of the admin interface.
    list_display = ('username', 'email', 'phone_number', 'company_name', 'category', 'is_staff')
    
    # Define the fields to be used for searching customers in the admin interface.
    search_fields = ('username', 'email', 'company_name', 'phone_number')
    
    # Define the fields that can be filtered in the admin interface.
    list_filter = ('category', 'is_staff', 'is_superuser')
    
    # Define the fields to be used in the Customer form.
    # These fields are displayed on the detail page of the admin interface.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'company_name', 'address', 'city', 'postal_code', 'gst_number', 'registration_number', 'category')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Define which fields should be displayed in the form for creating/editing users.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'company_name', 'address', 'city', 'postal_code', 'gst_number', 'registration_number', 'category'),
        }),
    )
    
    # Specify the model to use.
    model = Customer

# Register the Customer model with the custom admin settings.
admin.site.register(Customer, CustomerAdmin)
