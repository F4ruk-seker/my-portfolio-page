from django import template
from django.utils import timezone
from datetime import timedelta,date


register = template.Library()


@register.filter(name='WeeklyPlot')
def weekly_plot(page):
    start_of_week = timezone.now().date() - timedelta(days=timezone.now().weekday())
    end_of_week = start_of_week + timedelta(days=6)

    date_list = []
    for i in range((end_of_week - start_of_week).days + 1):
        date_list.append(start_of_week + timedelta(days=i))

    views = page.get_views_two_time_intervals(start_of_week,end_of_week)
    result = {}
    for date in date_list:
        result[date.day] = views.filter(visit_time__day=date.day).count()
    result = result.values()
    return result

