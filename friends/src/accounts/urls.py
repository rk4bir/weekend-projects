from django.conf.urls import url
from . import views
app_name = 'accounts'

urlpatterns = [
	url(r'^$', views.profile_view, name='index'),
	url(r"^activate/$", views.activateAccount_view, name='activate'),
	url(r"^change-password/$", views.passwordChange_view, name='change-password'),
	url(r"^forgot-password/$", views.passwordForgot_view, name='forgot-password'),
	url(r'^update/$', views.update_view, name='edit'),
	url(r'^login/$', views.userLogin_view, name='login'),
	url(r'^logout/$', views.userLogout_view, name='logout'),
	url(r'^register/$', views.userCreate_view, name='create'),
	url(r'^(?P<username>[a-z0-9._]+)/$', views.publicProfile_view, name='public-profile'),
]