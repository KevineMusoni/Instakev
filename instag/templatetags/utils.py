from django import template

register = template.Library()


@register.filter(name='has_liked')
def hliked(user, photo):
    for post in user.mylikes.all():
        if photo == post.photo:
            return True
    return False

@register.filter(name='has_saved')
def hsaved(user, photo):
    for post in user.saves.all():
        if photo == post.photo:
            return True
    return False