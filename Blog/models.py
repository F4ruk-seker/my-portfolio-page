from django.db import models
from autoslug import AutoSlugField
from mdeditor.fields import MDTextField


class BlogPost(models.Model):
    title = models.TextField()
    post = MDTextField()
    slug = AutoSlugField(populate_from='title')
    technologies = models.ManyToManyField('projects.Technologies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
