from django import template


register = template.Library()

@register.filter(name='TOTAL')
def total_list(list):
    return sum(list)