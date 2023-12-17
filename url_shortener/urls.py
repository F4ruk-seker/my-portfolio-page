from django.urls import path, include
from .views import ResponseRouter, UrlShorterAdminView

app_name = 'url_shortener'

urlpatterns = [
    path('admin/', UrlShorterAdminView.as_view()),
    path('<str:url>', ResponseRouter.as_view()),
]


