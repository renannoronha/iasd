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
        context['endereco'] = config.endereco
        context['facebook'] = config.facebook
        context['youtube'] = config.youtube
        context['twitter'] = config.twitter
        context['instagram'] = config.instagram
        context['nome'] = config.nome
        context['telefone'] = config.telefone
        context['email'] = config.email
        context['textoRodape'] = config.textoRodape
        context['horariosCulto'] = HorariosCulto.objects.all()
        return render(request, self.template_name, context)