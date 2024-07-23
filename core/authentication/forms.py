from django import forms
from .models import Customer

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'username', 'email', 'phone_number', 
            'company_name', 'address', 'city', 'postal_code', 'gst_number', 
            'registration_number', 'category'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customization: Add placeholders to all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'placeholder': self.fields[field].label})

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        # Validate that the passwords match
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Passwords do not match.')

        return cleaned_data