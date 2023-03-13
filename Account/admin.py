from django.contrib import admin
from Account.models import CustomUserModel
from Account import models
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    model = CustomUserModel
    # list_display = ('name',)
    # search_fields = ('name',)
    fieldsets = UserAdmin.fieldsets + (
        # ('notification', {
        #     'fields': ['can_sms','can_call','can_email','can_mobil_notification','phone_number']
        # }),
        ('özelleştirme',{
            'fields': ['avatar']
        }),
        ('Talent',{
            'fields': ['talent']
        }),
        ('Social Media', {
            'fields': ['SocialMedia']
        }),
    )

admin.site.register(models.SocialMedia)
admin.site.register(models.Talent)

# Register your models here.
