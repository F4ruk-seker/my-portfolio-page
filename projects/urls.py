from django.urls import path, include
from projects import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectListView.as_view(), name='ProjectsList'),
    path('<slug>/', views.ProjectDetailView.as_view(), name='ProjectDetailPage')
]



