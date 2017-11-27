from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^register/', views.register, name='register'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^editprofile/', views.editprofile, name='editprofile'),
	url(r'^change-password/', views.change_password, name='change_password'),
	url(r'^login/$', login, {'template_name':'personal/login.html'}),
	url(r'^logout/$', logout, {'template_name':'personal/logout.html'}),
	url(r'^reset-password/', password_reset, name='reset_password'),
	url(r'^reset-password/done/', password_reset_done, name='password_reset_done'),
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
	url(r'^reset-password/complete/', password_reset_complete, name='password_reset_complete'),
]
