from django.shortcuts import render

from base.models import pages

from Account.models import CustomUserModel, Talent, SocialMedia
from projects.models import Projects

from base.functions import view_counter_ruler

ViewCountWithRule = view_counter_ruler.ViewCountWithRule


def MainPageView(request):
    __page = pages.MainPage.objects.first()
    __talent = Talent.objects.all().order_by('priority')
    __SocialMedia = SocialMedia.objects.all().order_by('priority')

    counter = ViewCountWithRule(page=__page, request=request)
    counter()

    # __ip_address = get_client_ip(request)
    # __page.increase_view_count(__ip_address, request.user.is_authenticated)
    from Roadmap.models import RoadMapModel
    __my_roadmap = RoadMapModel.get_last_map()

    return render(request,'index.html', context={
        'page': __page,
        'portfolyo_user': CustomUserModel.objects.first(),
        'talents': __talent,
        'SocialMedia': __SocialMedia,
        'RoadMap': __my_roadmap
    })


def ProjectListView(request):
    __page = pages.ProjectsPage.objects.first()
    __projects = Projects.objects.all()
    counter = ViewCountWithRule(page=__page, request=request)
    counter()
    # __ip_address = get_client_ip(request)
    # __page.increase_view_count(__ip_address, request.user.is_authenticated)

    return render(request,'projectList.html',context={
        'page':__page,
        'projects':__projects
    })


def CVPageView(request):
    return render(request, 'CV.html')


def BlogPageView(request):
    return render(request,'blog.html')


