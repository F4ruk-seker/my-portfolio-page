from django.db import models
import string
import random
from django.contrib.sites.models import Site


class UrlModel(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField()
    router_url = models.URLField(default=None, blank=True, null=True)
    view = models.ManyToManyField('base.ViewModel', blank=True, default=None, editable=False)

    @staticmethod
    def create_random_router(length=12):
        charset = string.ascii_letters + string.digits
        return ''.join(random.choices(charset, k=length))

    def get_custom_url(self):
        return f'https://{Site.objects.first()}/r/{self.router_url}'

