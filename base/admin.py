from django.contrib import admin
from .models import pages, ViewModel

from django.utils.html import format_html


# def date_formatter(obj):
#     return format_html("<span style='color: red'>{}</span>".format(obj.created_at))
#
#
# class MessageModelAdmin(admin.ModelAdmin):
#     list_display = ('visit_time', 'ip_address')
#     readonly_fields = ('visit_time',)
#
#     def created_at(self, obj):
#         return date_formatter(obj)
#
#     created_at.short_description = 'Created At'
#
#
# admin.site.register(ViewModel, MessageModelAdmin)

page_list = filter(lambda name: name.endswith('Page') and name not in ['BasePage', 'CustomBasePage'], dir(pages))

for page in page_list:
    page_class = getattr(pages, page)

    class PageModelAdmin(admin.ModelAdmin):
        readonly_fields = ('created_at', 'view')

    admin.site.register(page_class, PageModelAdmin)

