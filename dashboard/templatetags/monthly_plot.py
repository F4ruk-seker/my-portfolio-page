from django import template
from django.utils import timezone
import datetime
from datetime import timedelta,date
from calendar import monthrange

register = template.Library()


@register.filter(name='MonthlyPlot')
def monthly_plot(page):
    today = timezone.now() # bugünün tarihi
    first_day_of_month = datetime.date(today.year, today.month, 1) # bu ayın ilk günü
    last_day_holder = monthrange(today.year, today.month)[1]
    last_day_of_month = datetime.date(today.year, today.month, last_day_holder )# bu ayın son günü
    # date_list = []

    date_list = [first_day_of_month + timedelta(days=i) for i in range((last_day_of_month - first_day_of_month).days + 1)]

    # for i in range((last_day_of_month - first_day_of_month).days + 1):
    #     date_list.append(first_day_of_month + timedelta(days=i))

    views = page.get_views_two_time_intervals(first_day_of_month, last_day_of_month)
    result = {}
    for date in date_list:
        result[date.day] = views.filter(visit_time__day=date.day).count()
    result = result.values()
    return result
    # return (0,2)

