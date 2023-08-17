from django.shortcuts import render,Http404
from base.models import pages


def dash(request):
    if request.user.is_authenticated:
        __pages_obj = [
            pages.MainPage,
            pages.ProjectsPage,
            pages.BlogPage,
            pages.CvPage,
        ]
        __pages = [page.objects.first() for page in __pages_obj]

        return render(request, 'dashboard-base.html',context={'pages': __pages})

    else:
        raise Http404()


