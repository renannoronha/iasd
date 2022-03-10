from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.sites.models import Site

from .models import *
from sermon.models import Sermon
from gallery.models import Gallery
from testimony.models import Testimony

# Create your views here.
class BaseView(View):
    def get_context_data(self, **kwargs):
        context = {
            'version': 1,
            'horariosCulto': HorariosCulto.objects.all(),
            'config': Config.objects.get(site=Site.objects.get_current()),
            'footerSermons': Sermon.objects.filter(ativo=True).order_by('-date')[:2]
        }
        return context

class HomeView(BaseView):
    template_name = 'home/home.html'
    title = 'Página Inicial'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        context['banners'] = Banner.objects.filter(ativo=True).order_by('ordem')
        context['secao1'] = PrimeiraSecao.objects.filter(site=Site.objects.get_current()).first()
        context['secao2'] = SegundaSecao.objects.filter(site=Site.objects.get_current()).first()
        context['secao3'] = TerceiraSecao.objects.filter(site=Site.objects.get_current()).first()
        context['secao4'] = Sermon.objects.filter(ativo=True).order_by('-date')[:3]
        context['secao5'] = Testimony.objects.all()[:10]
        context['secao6'] = None
        context['secao7'] = None
        context['secao8'] = Gallery.objects.filter(ativo=True)
        return render(request, self.template_name, context)