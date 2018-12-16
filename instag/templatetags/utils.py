from django import template

register = template.Library()

@register.filter(name='pos_saved')
def postsaved(user, photo):
    for post in user.saves.all():
        if photo == post.photo:
            return True
    return False