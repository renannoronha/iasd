from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.sites.models import Site

from .models import Config, HorariosCulto

# Create your views here.
class BaseView(View):
    def get_context_data(self, **kwargs):
        context = {
            'version': 1
        }
        return context

class HomeView(BaseView):
    template_name = 'home/home.html'
    title = 'Página Inicial'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        config = Config.objects.get(site=Site.objects.get_current())
        context['title'] = self.title + ' - ' + config.nome
        context['config'] = config
        context['horariosCulto'] = HorariosCulto.objects.all()
        return render(request, self.template_name, context)