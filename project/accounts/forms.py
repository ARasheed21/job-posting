from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CompanyInfo

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "id": "username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "password"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "name"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "password"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "confirm-password"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "email"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_regular')



class SignUpForm(UserCreationForm):
    
    is_admin = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'is_admin'}))
    is_regular = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'is_regular'}))
    
    company_name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'id': 'company-name'}))
    company_address = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'id': 'company-address'}))
    company_email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'id': 'company-email'}))
    company_logo = forms.URLField(required=False, widget=forms.TextInput(attrs={'id': 'company-logo'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_regular')

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.is_admin:
            company_info = CompanyInfo(
                name=self.cleaned_data['company_name'],
                address=self.cleaned_data['company_address'],
                email=self.cleaned_data['company_email'],
                logo=self.cleaned_data['company_logo']
            )
            if commit:
                company_info.save()
                user.company_info = company_info
        if commit:
            user.save()
        return user
