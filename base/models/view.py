from django.db import models
from dataclasses import dataclass
from requests import api
from config.settings.base import env, CUSTOM_LOGGER


class ViewModel(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.TextField()
    ip_query_id = models.TextField(null=True, blank=True, default=None)
    is_i_am = models.BooleanField(default=False)

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

    def save(self, *args, **kwargs):
        if response := api.get(env('IP_QUERY_SERVICE') + self.ip_address):
            try:
                self.ip_query_id = response.json().get('_id')
            except Exception as ERR:
                CUSTOM_LOGGER.construct(
                    title='ip query service',
                    error=ERR,
                    metadata=f'{self.ip_address}, {response.text}, {response}'
                )
                CUSTOM_LOGGER.send()
        super().save(*args, **kwargs)

