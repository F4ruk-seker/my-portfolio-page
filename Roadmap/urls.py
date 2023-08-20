from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mindmap'
urlpatterns = [
    path('', views.AllMindMapsListView.as_view(), name='AllMindMaps'),
    path('<slug>/', views.MindMapView.as_view(), name='MindMap'),

]
