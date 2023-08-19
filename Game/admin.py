from django.contrib import admin
from Game.models import *


admin.site.register(GameTypeModels)
admin.site.register(GameInfoModel)
admin.site.register(GameVideoModel)
admin.site.register(Game)


@admin.register(MusicInfoModel)
class MusicInfoModelAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'image', 'url', 'length']  # Tüm alanları görüntüle

    def save_model(self, request, obj, form, change):
        if obj.url:  # URL alanı doldurulmuşsa
            print("called")
            super().save_model(request, obj, form, change)
        else:
            self.message_user(request, "URL alanı doldurulmalıdır.", level='ERROR')