from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from Auth import views as auth_view



urlpatterns = [
    path('admin/login/', auth_view.CustomAdminLogin.as_view(),name='login'),
    path('admin/otp/', auth_view.OTPView.as_view(),name='otp-admin'),
    path('admin/', admin.site.urls),
    path('', include('Portfolyo.urls')),
    path('message/', include('Communication.urls')),
    path('dashboard/', include('dashboard.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


