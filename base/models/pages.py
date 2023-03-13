from cloudinary.models import CloudinaryField
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.apps import apps
# Create your models here.
from django.utils import timezone
from datetime import timedelta,date


class BasePage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False,null=True)
    view = models.ManyToManyField('base.ViewModel',blank=True,default=None,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ceo
    keywords = models.TextField(blank=False,null=True)
    robots = models.TextField(blank=False,null=True)
    # description = models.TextField(blank=False,null=True)
    # sulg = models.TextField(blank=False,null=True)
    image = CloudinaryField("image",
        overwrite=True,
        folder='portfolyo/page/ceo',
        resource_type="image",
        transformation={"quality": "auto:low"},
        format="webp", )
    image_alt = models.TextField(blank=False,null=True)

    def get_view_count(self):
        return self.view.count()

    def get_views_two_time_intervals(self,start_of_date,end_of_date):
        return self.view.all().filter(visit_time__range=[start_of_date, end_of_date])

    def get_views_today_hourly(self):
        today = datetime.today()
        return self.view.all().filter(visit_time__day=today.day).order_by('visit_time')

    def get_views_this_weekly(self):
        start_of_week = timezone.now().date() - timedelta(days=timezone.now().weekday())
        end_of_week = start_of_week + timedelta(days=6)
        return self.view.all().filter(visit_time__range=[start_of_week, end_of_week])

    # def get_views_this_monthly(self):
    #     today = timezone.now().date()
    #     start_of_month = date(today.year, today.month, 1)
    #     end_of_month = date(today.year, today.month, 28) + timedelta(days=4)
    #     end_of_month = end_of_month - timedelta(days=end_of_month.day)
    #     return self.view.all().filter(visit_time__range=[start_of_month, end_of_month])

    def increase_view_count(self,ip):
        self.view.create(ip_address=ip)


    def __str__(self):
        return f'{self.title} ○ Settings'

    class Meta:
        abstract = True


class MainPage(BasePage):
    top_3_projects = models.ManyToManyField('projects.Projects',blank=True)
    def get_top_projects(self):
        return self.top_3_projects.all()[:3]


class ProjectsPage(BasePage):
    pass


class BlogPage(BasePage):
    pass


class CvPage(BasePage):
    pass


