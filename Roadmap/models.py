from django.db import models
from mdeditor import fields as md_fields


class RoadMapModel(models.Model):
    name = models.TextField()
    created = models.DateField(auto_created=True)
    md = md_fields.MDTextField()  # test

    @staticmethod
    def get_last_map():
        return RoadMapModel.objects.all().order_by('created').first()