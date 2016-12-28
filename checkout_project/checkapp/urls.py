from django.conf.urls import url
from checkapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^checkout/(?P<pk>\d+)/$', views.computer_detail, name='computer_detail'),
    url(r'^checkout/(?P<pk>\d+)/checkout/$', views.computer_checkout, name='computer_checkout'),
    url(r'^checkin/$', views.checkin, name='checkin'),
    url(r'^checkin/(?P<pk>\d+)/$', views.computer_checkin_detail, name='computer_checkin_detail'),
    url(r'^checkin/(?P<pk>\d+)/checkin/$', views.computer_checkin, name='computer_checkin'),
    url(r'^asset_new/$', views.asset_new, name='asset_new'),
]
