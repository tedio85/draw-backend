from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^entrance/$', views.EntranceView.as_view(), name='entrance'),
]