from django import forms
from .models import Medicine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email address', required=True, widget=forms.EmailInput)
    first_name = forms.CharField(label='First Name', required=True, widget=forms.TextInput)
    last_name = forms.CharField(label='Last Name', required=True, widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput)
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)

    
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'description','price']
