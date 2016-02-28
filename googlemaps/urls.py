from django.conf.urls import patterns, include, url
from views import HomeView, MapView

urlpatterns = [
	url(r'^$', MapView.as_view(), name='map'),
]