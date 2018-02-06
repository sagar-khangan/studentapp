from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^filter/$', MyListView.as_view(), name='filter'),
    url(r'^delete/(?P<pk>[0-9]+)/$', MyDeleteView.as_view(), name='delete'),
    url(r'^update/(?P<pk>[0-9]+)/$', MyUpdatateView.as_view(), name='update'),
    # url(r'^filter/(?P<text>[a-zA-Z]+)/$', MyListView.as_view(), name='filter')
]