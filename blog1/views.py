from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    TemplateView,
    ListView,
    UpdateView,
    CreateView,
    DetailView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from blog1.models import Post


# Create your views here.
# home as function based view
def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog1/home.html', context)


# home as a class based view
class Home(ListView):
    '''Home View where all posts are listed'''
    model = Post
    ordering = ['-date_posted']
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog1/home.html'


class UserPostListView(ListView):
    '''lists out posts by a given user'''
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog1/user_posts.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    '''to list details of a given post on a page'''
    model = Post


class PostCreateView(CreateView):
    '''View to create a post featuring a form with field of title and content'''
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''Update a given post with form fields of  title and content'''
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''View to delete a given post'''
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# about as a function based view
def about(request):
    return render(request, 'blog1/about.html', {'title': 'about'})


class About(TemplateView):
    '''About the blog'''
    template_name = "blog1/about.html"
