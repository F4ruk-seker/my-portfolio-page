from django.contrib import admin
from Roadmap.models import RoadMapModel


# admin.site.register(RoadMapModel)


@admin.register(RoadMapModel)
class RoadMapModelAdmin(admin.ModelAdmin):
    # list_display = ['']
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    readonly_fields = ['created']
    # search_fields = ['']
    # ordering = ['']
