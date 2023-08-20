from django.http import Http404
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from Roadmap.models import RoadMapModel


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
        if not (obj.can_share or self.request.user.is_authenticated):
            raise Http404("This roadmap is not valid.")
        return obj
