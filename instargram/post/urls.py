from django.conf.urls import url
from . import views


app_name = 'post'
urlpatterns = [
    # post
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<post_pk>\d+)/modify/$', views.post_modify, name='post_modify'),

    # comment
    url(r'^(?P<post_pk>\d+)/comment-create/$', views.comment_create, name='comment_create'),
    url(r'^(?P<comment_pk>\d+)/comment-modify/$', views.comment_modify, name='comment_modify'),

    # post like & unlike
    url(r'^(?P<post_pk>\d+)/post-like-toggle/$', views.post_like_toggle, name='post_like_toggle'),
]