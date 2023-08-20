from django.db import models
from mdeditor import fields as md_fields
from autoslug import AutoSlugField
from django.utils.text import slugify


class RoadMapModel(models.Model):
    name = models.TextField()
    slug = AutoSlugField(
        populate_from='name',  # Use 'name' field to populate the slug
        slugify=slugify,  # Use the slugify function from Django's utils
        editable=True
    )
    created = models.DateField(auto_now_add=True)  # Use auto_now_add for creation date
    can_share = models.BooleanField(default=False)
    md = md_fields.MDTextField()  # test
