from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView, FormView
from .models import UrlModel
from .forms import UrlShorterForm
from django.http import Http404
from base.functions.view_counter_ruler import ViewCountWithRule
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ResponseRouter(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if url :=kwargs.get('url'):
            if router := UrlModel.objects.filter(
                router_url=url
            ).first():
                counter = ViewCountWithRule(router, self.request)
                counter()
                return router.url

        raise Http404


class UrlShorterAdminView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'router_admin.html'
    form_class = UrlShorterForm
    success_url = '/r/admin/'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_shorteners_statistics'] = UrlModel.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        print('is post')
        form = self.get_form()
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)