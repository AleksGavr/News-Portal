from django import template

# если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются
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

# for word in in_text.split():
#     if word.lower() in bad_text:
#         in_text = in_text.replace(
#             word,
#             f'{word[0]}{"*" * (len(word) - 1)}'
#         )
# return in_text
