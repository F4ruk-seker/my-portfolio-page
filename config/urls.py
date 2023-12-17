from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from Auth import views as auth_view


urlpatterns = [
    path('admin/', auth_view.FakeAdminLogin.as_view(), name='fake_login'),
    path('raden/login/', auth_view.CustomAdminLogin.as_view(), name='login'),
    path('raden/otp/', auth_view.OTPView.as_view(), name='otp-admin'),
    path('raden/', admin.site.urls),
    path('', include('Portfolyo.urls')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('message/', include('Communication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('mind-map/', include('Roadmap.urls')),
    path('game/', include('Game.urls')),
    path('r/', include('url_shortener.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


