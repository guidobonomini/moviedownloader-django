from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'home/$', views.index, name='index'),
    url(r'searchYTS/(?P<query>[\w\ ]+)/(?P<currentPage>[0-9]+)/$', views.searchYTS, name="searchYTS"),
    url(r'searchPirateBay/(?P<query>[\w\ ]+)/(?P<currentPage>[0-9]+)/$', views.searchPirateBay, name="searchPirateBay"),
    url(r'searchSubdivx/(?P<query>.*)/(?P<currentPage>[0-9]+)/$', views.searchSubdivx, name="searchSubdivx"),
]
