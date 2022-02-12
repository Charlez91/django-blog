from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('feeds/', views.feeds, name='blog-feeds'),
    path('login/', views.login, name='blog-login')

]