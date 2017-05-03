from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<pk>\d+)/(?P<name>\w+)/$', views.profile, name='account_landing'),
    url(r'^account_redirect/$', views.account_redirect, name='account_redirect'),
    url(r'^redirect_to_third_party_api/$', views.redirect_to_third_party_api, \
    name='redirect_to_third_party_api'),
    url(r'^login/$', auth_views.login, {'template_name':'movies/login.html'}, name='login'),
]
