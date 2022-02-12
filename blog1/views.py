from django.shortcuts import render

posts = [
	{
		'author':'Charles Okeke',
		'title':'Blog Post 1',
		'content': 'First Post Content',
		'date_posted': 'March 16, 2021'
	},
	{
		'author':'Chinedu Okeke',
		'title':'Blog Post 2',
		'content': 'Second Post Content',
		'date_posted': 'March 17, 2021'
	},
	{
		'author': 'Ezinne Okeke',
		'title': 'Blog Post 3',
		'content': 'First Post Content',
		'date_posted': 'March 18, 2021'
	}
]

# Create your views here.

def home(request):
	context = {
		'posts':posts
	}
	return render(request, 'blog1/home.html', context )

def about(request):
	return render(request, 'blog1/about.html', {'title' : 'about'})

def feeds(request):
	return render(request, 'blog1/feeds.html')

def login(request):
	return render(request, 'blog1/login.html')