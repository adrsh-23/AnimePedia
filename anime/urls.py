from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('create_page',views.create_page,name="create_page"),
    path('create',views.create,name="create"),
    path('delete/<str:anime_id>',views.delete,name="delete"),
    path('edit/<str:anime_id>',views.edit,name="edit"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('register',views.register,name="register"),
    path('upvote/<str:anime_id>',views.upvote,name="upvote"),
    path('sortAnime/<str:type>',views.sortAnime,name="sortAnime"),
]
