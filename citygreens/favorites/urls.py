from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/(?P<product_id>\d+)/$', views.favs_add, name='favs_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.favs_remove, name='favs_remove'),
    url(r'^details/$', views.favs_list, name='favs_list')
]