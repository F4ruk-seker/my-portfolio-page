from django.shortcuts import render
from django.views.generic import DetailView, ListView

from base.functions.view_counter_ruler import ViewCountWithRule
from projects.models import Projects
from base.models.pages import ProjectsPage


class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'projects_detail.html'
    context_object_name = 'project'


class ProjectListView(ListView):
    model = Projects
    queryset = Projects.objects.all()
    context_object_name = 'projects'
    template_name = 'projectList.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=None, **kwargs)
        context['page'] = ProjectsPage.objects.first()

        counter = ViewCountWithRule(page=context['page'], request=self.request)
        counter()

        return context
