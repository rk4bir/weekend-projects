from django.conf.urls import url
from . import views
app_name = 'comments'

urlpatterns = [
	url(r'^create/$', views.create_view, name='create'),
	url(r'^reply-create/$', views.replyCreate_view, name='reply-create'),
	url(r'^(?P<slug>[\w-]+)/edit/$', views.edit_view, name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete_view, name='delete'),
]