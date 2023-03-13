from django.urls import path
from Auth.api.views import login

app_name = "Auth-Api"
urlpatterns = [
    path('login',login,name='api-login'),

]
