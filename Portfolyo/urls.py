from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainPageView, name='MainPage'),
    path('blog/', views.BlogPageView, name='BlogList'),
    path('cv/', views.CVPageView, name='CVPage'),
]


