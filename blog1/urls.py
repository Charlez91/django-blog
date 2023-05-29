from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.Home.as_view(), name='blog-home'),
    path('about/', views.About.as_view(), name='blog-about'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
    path('post/new/', login_required(views.PostCreateView.as_view()), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('search/', views.search, name='search')

]
