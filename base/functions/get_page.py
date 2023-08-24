from django.shortcuts import Http404
from base.models import pages


def get_page_or_404(page):
    if page is not str:
        page = page.__name__
    page = getattr(pages, page)
    if page is not None:
        if page := page.objects.first():
            return page
    raise Http404('page is has been deleted')

