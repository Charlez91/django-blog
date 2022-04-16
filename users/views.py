from django.shortcuts import render, redirect
from django.contrib import messages
from blog1.models import Post
from users.forms import UserRegistrationForm



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}!')
            return redirect ('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})