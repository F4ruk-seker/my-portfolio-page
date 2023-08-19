from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainPageView, name='MainPage'),
    path('blog/', views.BlogPageView, name='BlogList'),
    path('projects/', views.ProjectListView, name='ProjectsList'),
    path('cv/', views.CVPageView, name='CVPage'),
    path('game/', views.GamePageView, name='GamePage'),
]
