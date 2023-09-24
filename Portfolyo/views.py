from django.shortcuts import render
from django.shortcuts import get_object_or_404
from base.functions import get_page_or_404
from base.models import pages
from Game.models import Game
from Account.models import CustomUserModel, Talent, SocialMedia
from projects.models import Projects

from base.functions import view_counter_ruler

ViewCountWithRule = view_counter_ruler.ViewCountWithRule
import logging

logger = logging.getLogger('django')
import mistune


def MainPageView(request):
    __page = get_page_or_404(pages.MainPage)
    __talent = Talent.objects.all().order_by('priority')
    __SocialMedia = SocialMedia.objects.all().order_by('priority')
    counter = ViewCountWithRule(page=__page, request=request)
    counter()
    # __ip_address = get_client_ip(request)
    # __page.increase_view_count(__ip_address, request.user.is_authenticated)

    __my_roadmap = __page.road_map
    print(request.META)
    return render(request, 'index.html', context={
        'page': __page,
        'portfolyo_user': CustomUserModel.objects.first(),
        'talents': __talent,
        'SocialMedia': __SocialMedia,
        'RoadMap': __my_roadmap,
    })




def CVPageView(request):

    return render(request, 'CV.html')


def BlogPageView(request):
    return render(request,'blog.html')


