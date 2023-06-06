from django.shortcuts import render

from base.models import pages

from Account.models import CustomUserModel,Talent,SocialMedia
from projects.models import Projects


def MainPageView(request):
    __page = pages.MainPage.objects.first()
    __talent = Talent.objects.all().order_by('priority')
    __SocialMedia = SocialMedia.objects.all().order_by('priority')

    __ip_address = get_client_ip(request)
    __page.increase_view_count(__ip_address)

    return render(request,'index.html',context={
        'page':__page,
        'portfolyo_user':CustomUserModel.objects.first(),
        'talents':__talent,
        'SocialMedia':__SocialMedia
    })

def ProjectListView(request):
    __page = pages.ProjectsPage.objects.first()
    __projects= Projects.objects.all()

    __ip_address = get_client_ip(request)
    __page.increase_view_count(__ip_address)

    return render(request,'projectList.html',context={
        'page':__page,
        'projects':__projects
    })


def CVPageView(request):
    return render(request,'CV.html')


def BlogPageView(request):
    return render(request,'blog.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


