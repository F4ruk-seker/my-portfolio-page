from django.contrib import admin
from .models import pages,ViewModel

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



admin.site.register(pages.MainPage)
admin.site.register(pages.ProjectsPage)
admin.site.register(pages.CvPage)
admin.site.register(pages.BlogPage)
# Register your models here.
