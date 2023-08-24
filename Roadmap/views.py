from django.http import Http404
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from Roadmap.models import RoadMapModel
from base.functions.view_counter_ruler import ViewCountWithRule

from django.views.decorators.clickjacking import xframe_options_exempt

class AllMindMapsListView(ListView):
    model = RoadMapModel
    template_name = 'mindmap_list_view.html'
    context_object_name = 'mind_map_list'


class MindMapView(DetailView):
    model = RoadMapModel
    template_name = 'mindmap_view.html'
    context_object_name = 'map'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        counter = ViewCountWithRule(obj, self.request)
        counter()

        if not (obj.can_share or self.request.user.is_authenticated):
            raise Http404("This roadmap is not valid.")
        return obj

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

