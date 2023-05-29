from django import template
from datetime import datetime

register = template.Library()

# @register.filter
# def lower(value):
#     return value.lower()

@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)

forbidden_words = [
    'плохой',
    'гадкий'
]

@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)