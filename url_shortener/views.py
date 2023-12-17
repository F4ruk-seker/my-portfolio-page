from django.shortcuts import render
from django.views.generic import RedirectView
from .models import UrlModel
from django.http import Http404


class ResponseRouter(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if url :=kwargs.get('url'):
            if router := UrlModel.objects.filter(
                router_url=url
            ).first():
                return router.url

        raise Http404

