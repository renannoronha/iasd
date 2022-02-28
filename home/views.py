from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.sites.models import Site

from .models import *

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
        context['banners'] = Banner.objects.filter(ativo=True).order_by('ordem')
        context['secao1'] = PrimeiraSecao.objects.filter(site=Site.objects.get_current()).first()
        context['secao2'] = SegundaSecao.objects.filter(site=Site.objects.get_current()).first()
        context['secao3'] = TerceiraSecao.objects.filter(site=Site.objects.get_current()).first()
        context['secao4'] = None
        context['secao5'] = None
        context['secao6'] = None
        context['secao7'] = None
        context['secao8'] = None
        return render(request, self.template_name, context)