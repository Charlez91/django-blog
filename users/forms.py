from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    """docstring for UserRegistrationForm"""
    '''def __init__(self, arg):
        super(UserRegistrationForm, self).__init__()
        self.arg = arg'''
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    """docstring for UserRegistrationForm"""
    '''def __init__(self, arg):
        super(UserRegistrationForm, self).__init__()
        self.arg = arg'''
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    # image = forms.ImageField()
    # tests = forms.DateField()
    """docstring for UserRegistrationForm"""
    '''def __init__(self, arg):
        super(UserRegistrationForm, self).__init__()
        self.arg = arg'''
    class Meta:
        model = Profile
        fields = ['image']
