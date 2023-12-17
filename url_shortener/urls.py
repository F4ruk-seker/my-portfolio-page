from django.urls import path, include
from .views import ResponseRouter

app_name = 'url_shortener'
urlpatterns = [
    path('<str:url>', ResponseRouter.as_view())

]



