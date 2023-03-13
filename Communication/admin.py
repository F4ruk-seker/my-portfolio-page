from django.contrib import admin
from .models import Message

from django.utils.html import format_html


def date_formatter(obj):
    return format_html("<span style='color: red'>{}</span>".format(obj.created_at))


class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'Subject', 'created_at',)
    readonly_fields = ('created_at',)

    def created_at(self, obj):
        return date_formatter(obj)

    created_at.short_description = 'Created At'


admin.site.register(Message, MessageModelAdmin)

# Register your models here.
