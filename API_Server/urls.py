from django.conf.urls import patterns, url
from views import  *
urlpatterns = [

    url(r'^server/$', server_list, name='server_list'),
    url(r'^server/(?P<name>\w+)/$', server_detail, name='server_detail'),
]
