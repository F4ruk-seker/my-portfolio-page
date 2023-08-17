from django.db import models


class ViewModel(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.TextField()
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


    def save(self,
  *args, **kwargs
):
        print(self)
        print(self.visit_time)
        print(self.is_i_am)
        print(self.ip_address)
        super().save(*args, **kwargs)