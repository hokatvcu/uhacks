from django.conf.urls import patterns, include, url
from views import HomeView, MapView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^map/$', MapView.as_view(), name='map'),
]