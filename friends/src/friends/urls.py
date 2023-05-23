from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from main import views


urlpatterns = [
	url(r'^$', views.home_view, name='homepage'),
	url(r'^404-not-found/$', views.ErrorNotFound_view, name='404NotFound'),
	url('admin/', admin.site.urls),
	url(r'^accounts/', include('accounts.urls')),
	url(r'^comments/', include('comments.urls')),
	url(r'^contact-us/$', views.contactUs_view, name='contact-us'),
	url(r'^notifications/$', views.notifications_view, name='notifications'),
	url(r'^notifications/(?P<pk>[0-9]+)/$', views.notificationStatus_view, name='notf-seen'),
	url(r'^posts/', include('posts.urls')),
	url(r'^search/$', views.search_view, name='search'),
	url(r'^valildatename/$', views.valildateName_view, name='valildate-name'),
	url(r'^valildateemail/$', views.valildateEmail_view, name='valildate-email'),
	url(r'^valildatepassword/$', views.valildatePassword_view, name='valildate-password'),

]

"""
if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
"""