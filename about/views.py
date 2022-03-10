from django.shortcuts import render
from home.views import BaseView
from .models import *

from testimony.models import Testimony

# Create your views here.
class AboutView(BaseView):
    template_name = 'about/about.html'
    title = 'Sobre'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        context['secao1'] = AboutPrimeiraSecao.objects.filter(site=Site.objects.get_current()).first()
        context['secao2'] = AboutSegundaSecao.objects.filter(site=Site.objects.get_current()).first()
        context['secao3'] = AboutTerceiraSecao.objects.filter(site=Site.objects.get_current()).first()
        context['secao4'] = Pastor.objects.all()
        context['secao5'] = Testimony.objects.all()[:10]
        return render(request, self.template_name, context)