from django.shortcuts import render
from blog1.models import Post
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
	context = {
		'posts':Post.objects.all()
	}
	return render(request, 'blog1/home.html', context )


def about(request):
	return render(request, 'blog1/about.html', {'title' : 'about'})


def feeds(request):
	return render(request, 'blog1/feeds.html')


def login(request):
	return render(request, 'blog1/login.html')