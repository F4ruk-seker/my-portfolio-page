import json

from django.db import models
from dataclasses import dataclass
from requests import api
from config.settings.base import env, CUSTOM_LOGGER
from base.functions import get_ip_data


class ViewModel(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.TextField()
    # ip_query_id = models.TextField(null=True, blank=True, default=None)
    ip_data = models.TextField(null=True, default=None, blank=True)
    is_i_am = models.BooleanField(default=False)
    user_agent = models.TextField(null=True, default=None, blank=True, editable=False)

    def __str__(self):
        visited_time = self.visit_time.strftime("%Y-%B-%d %H:%M")
        months = {
            'January': 'Ocak',
            'February': 'Şubat',
            'March': 'Mart',
            'April': 'April',
            'May': 'Mayıs',
            'June': 'Haziran',
            'July': 'Temmuz',
            'August': 'Ağustos',
            'September': 'Eylül',
            'October': 'Ekim',
            'November': 'Kasım',
            'December': 'Aralık',
        }

        for month, turkish in months.items():
            visited_time = visited_time.replace(month, turkish)

        return f'{self.ip_address} | {visited_time} '

    def save_ip_data(self, *args, **kwargs):
        try:
            self.ip_data = get_ip_data(self.ip_address)
        except Exception as ERR:
            CUSTOM_LOGGER.construct(
                title='ip query service',
                error=ERR,
                metadata=f'{self.ip_address}'
            )
            CUSTOM_LOGGER.send()

    def save(self, *args, **kwargs):
        self.save_ip_data()
        super().save(*args, **kwargs)

    @staticmethod
    def ip_query_service_url() -> str:
        return env('IP_QUERY_SERVICE')

