from django.contrib import admin
from Auth.models import AuthToken
from Auth.models import OTPDevice

admin.site.register(AuthToken)
admin.site.register(OTPDevice)

# Register your models here.
