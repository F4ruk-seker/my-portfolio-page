from django.views.generic import TemplateView
from django.shortcuts import reverse, redirect
from base.models.pages import FakeAdminLoginPage
from base.functions.view_counter_ruler import ViewCountWithRule


class FakeAdminLogin(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        ViewCountWithRule(FakeAdminLoginPage.objects.first(), self.request)()
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return redirect(reverse('fake_login'))

