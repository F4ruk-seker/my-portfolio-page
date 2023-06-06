from django import template
from django.utils import timezone
import datetime
from datetime import timedelta,date
from calendar import monthrange
import calendar


register = template.Library()


@register.filter(name='YearlyPlot')
def yearly_plot(page):
    year = timezone.now().year # bugünün tarihi
    # if today.year % 4 == 0:
    #     DAYS_COUNT = 364
    # else:
    #     DAYS_COUNT = 365
    DAYS_COUNT = 364 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 365

    # first_day_of_month = datetime.date(today.year, today.month, 1) # bu ayın ilk günü
    # last_day_holder = monthrange(today.year, today.month)[1]
    # last_day_of_month = datetime.date(today.year, today.month, last_day_holder )# bu ayın son günü
    # # date_list = []
    first_day_of_year = datetime.date(year, 1, 1) # bu yılın ilk günü
    last_day_of_year = datetime.date(year, 12, 30) if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else datetime.date(year, 12, 31)


    date_list = [first_day_of_year + timedelta(days=i) for i in range((last_day_of_year - first_day_of_year).days + 1)]
    #
    # # for i in range((last_day_of_month - first_day_of_month).days + 1):
    # #     date_list.append(first_day_of_month + timedelta(days=i))
    #
    # views = page.get_views_two_time_intervals(first_day_of_year, last_day_of_year)
    # result = {}
    # counter = 0
    # for date in date_list:
    #     result[date.day] = views.filter(visit_time__day=date.day).count()
    #     counter += 1
    # result = result.values()
    result = [
        [x for x in range(30)],
        [x for x in range(31)],
        [x for x in range(25)]
    ]
    return result
    # return (0,2)

