from django import template

register = template.Library()

censor_words = [
    'санкций',
    'убийство',
]


@register.filter()
def censor(value):
    text = str.split(value)
    for cw in text:
        if cw.lower() in censor_words:
            value = value.replace(cw, cw[0] + '*' * (len(cw) - 1))
    return value
