from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^myaccount/$', views.mine, name='myaccount'),
    url(r'^myaccount/edit/$', views.edit, name='edit'),
    url(r'^comment/(?P<post_id>\d+)$', views.comment_on, name='comment'),
    url(r'^user/(?P<user_id>\d+)$', views.user, name='aboutuser'),
    url(r'^like/(?P<post_id>\d+)$', views.like, name='like'),
    url(r'^save/(?P<post_id>\d+)$', views.save, name='save'),
    url(r'^search/(?P<name>.+)$', views.find, name='save'),
    url(r'^follow_or_not/(?P<user_id>\d+)$', views.togglefollow, name='follow_or_not'),
    url(r'^unlike/(?P<post_id>\d+)$', views.unlike, name='unlike')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
