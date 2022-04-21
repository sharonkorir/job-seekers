
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from seekers.models import User

#update profile email and username
class UserRegistrationForm(UserCreationForm):
    '''
    Form that inherits from the django UserCreationForm and adds email field 
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
