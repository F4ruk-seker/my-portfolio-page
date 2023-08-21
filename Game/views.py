from django.shortcuts import render
from django.views.generic import ListView, DetailView

from Account.models import CustomUserModel
from Game.models import *
from base.functions.view_counter_ruler import ViewCountWithRule


class GameListView(ListView):
    # model = Game.objects.all
    queryset = Game.objects.all()
    context_object_name = 'game_list'
    template_name = 'main_page.html'

    def get_context_data(self, *args, object_list=None, **kwargs):

        context = super().get_context_data(*args, object_list=None, **kwargs)
        context['portfolyo_user'] = CustomUserModel.objects.first()

        return context


class GameVideoView(DetailView):
    model = Game

    # queryset = Game.objects.all()
    context_object_name = 'game'
    template_name = 'game_video.html'

    def get_context_data(self, *args, object_list=None, **kwargs):

        context = super().get_context_data(*args, object_list=None, **kwargs)
        context['portfolyo_user'] = CustomUserModel.objects.first()

        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        ViewCountWithRule(obj, self.request)()
        return obj
