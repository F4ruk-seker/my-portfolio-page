from django.urls import path
from Auth.views import LoginView,Logout

app_name = "Auth"
urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
    # path('create/',createLoginToken.as_view(),name='create'),
]
