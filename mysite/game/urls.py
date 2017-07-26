from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^entrance/$', views.EntranceView.as_view(), name='entrance'),
    url(r'^over/$', RedirectView.as_view(url='/game/entrance/')),
]