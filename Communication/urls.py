from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('new/', views.NewMessage.as_view(), name='message-new'),
    # path('all/', views.MainPageView, name='message-list'),
    # path('<uuid:uuid>/', views.MainPageView, name='message-detail'),
]
