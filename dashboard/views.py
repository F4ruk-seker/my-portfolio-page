from django.shortcuts import render, Http404
from base.models import pages
from config.settings.base import env


def dash(request):
    if request.user.is_authenticated:
        page_list = filter(lambda name: name.endswith('Page') and name not in ['BasePage', 'CustomBasePage'],
                           dir(pages))
        page_list = [getattr(pages, page).objects.first() for page in page_list]
        return render(request, 'dashboard-base.html',
                      context={'pages': page_list, 'ip_query_service_url': env('IP_QUERY_SERVICE')})
    else:
        raise Http404()

