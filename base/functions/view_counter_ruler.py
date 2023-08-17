from base.models import ViewModel
from django.utils.timezone import now


class ViewCountWithRule:
    def __init__(self, page, request):
        self.page = page
        self.request = request
        self.ip_address = self.get_client_ip()

    def can(self):
        if vs := ViewModel.objects.filter(ip_address=self.ip_address).order_by('-visit_time').first():
            return vs.visit_time.hour not in [now().hour - 1, now().hour]

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def is_admin_user(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def action(self):
        if self.can():
            _ = ViewModel.objects.create(visit_time=now(), ip_address=self.ip_address, is_i_am=self.is_admin_user())
            self.page.view.add(_)

    def __call__(self, *args, **kwargs):
        self.action()

