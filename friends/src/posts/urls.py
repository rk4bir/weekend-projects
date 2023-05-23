from django.conf.urls import url
from . import views
app_name = 'posts'

urlpatterns = [
	url(r'^$', views.postList_view, name='list'),
	url(r'^create/$', views.createPost_view, name='create'),
	url(r'^(?P<slug>[\w-]+)/$', views.detail_view, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.edit_view, name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete_view, name='delete'),
    url(r'^(?P<slug>[\w-]+)/like/$', views.like_view, name='like'),
]


