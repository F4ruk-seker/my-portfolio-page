from django.contrib import admin
from .models import UrlModel
from .forms import UrlShorterForm
from django.utils.html import format_html
from django.contrib.sites.models import Site


@admin.register(UrlModel)
class UrlModelAdmin(admin.ModelAdmin):

    form = UrlShorterForm
    readonly_fields = ('router_url', 'router_url_with_link', 'view_count', 'view')

    def router_url_with_link(self, obj):
        if obj.router_url:
            return format_html('<a href="{0}" target="_blank">{0}</a>'.format(f'https://{Site.objects.first()}/r/{obj.router_url}'))
        else:
            return None

    router_url_with_link.allow_tags = True
    router_url_with_link.short_description = 'Router URL Link'

    def view_count(self, obj):
        return obj.view.count()

    view_count.short_description = 'View Count'
