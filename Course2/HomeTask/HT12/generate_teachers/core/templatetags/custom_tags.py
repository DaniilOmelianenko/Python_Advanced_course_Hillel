import re

from core.models import Teacher

from django import template


register = template.Library()


@register.filter
def even_numbers(enter_list):
    enter_list = (re.sub("[ ,.]", " ", enter_list))
    enter_list = enter_list.split()
    enter_list = [int(x) for x in enter_list]
    new_list = [x for x in enter_list if x % 2 == 0]
    return new_list


@register.filter
def number_of_words(string):
    return str(len(string.split()))


@register.inclusion_tag(filename='includes/teacher_filtering.html')
def random_teachers(count=5):
    return {
        'teachers': Teacher.objects.all().order_by('?')[:count]
    }


@register.simple_tag
def query_filter_simple(query, **kwargs):
    return query.filter(**kwargs)


@register.inclusion_tag(filename='includes/student_filtering.html')
def query_filter_inclision(query, **kwargs):
    return {
        'students': query.filter(**kwargs)
    }
