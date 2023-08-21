from django.contrib import admin
from django.urls import path, include
from . import views

app_name: str = 'game'
urlpatterns = [
    path('', views.GameListView.as_view(), name='GameListPage'),
    path('<uuid:pk>/', views.GameVideoView.as_view(), name='GameVideoPage'),
]
