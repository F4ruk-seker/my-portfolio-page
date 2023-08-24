from django.shortcuts import render, Http404
from base.models import pages


def dash(request):
    if request.user.is_authenticated:
        page_list = filter(lambda name: name.endswith('Page') and name not in ['BasePage', 'CustomBasePage'],
                           dir(pages))
        page_list = [getattr(pages, page).objects.first() for page in page_list]
        return render(request, 'dashboard-base.html',context={'pages': page_list})
    else:
        raise Http404()

