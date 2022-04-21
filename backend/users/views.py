from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from seekers.models import User
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    '''
    Register a new user on registration and create user profile using signals
    '''
    if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
        form.save()
        #username = form.cleaned_data.get('username')
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        #succesful log in message
        messages.success(request, f'Your Jobseekers account had been created successfully')
        
        return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
    

