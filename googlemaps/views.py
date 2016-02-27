from django.shortcuts import render
from django.views.generic.base import TemplateView
from hackathons.models import Hackathon

# Create your views here.
class HomeView(TemplateView):

    template_name = 'uhacks/home.html'

class MapView(TemplateView):

    template_name = 'uhacks/map.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MapView, self).get_context_data(*args, **kwargs)
        context['hackathons'] = Hackathon.objects.all()
        return context