from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class BaseView(View):
    def get_context_data(self, **kwargs):
        context = {
            'version': 1
        }
        return context

class HomeView(BaseView):
    template_name = 'home/home.html'
    title = 'Página Inicial - IASD Central de Foz'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title
        context['endereco'] = 'Av. República Argentina, 552 85851-200 Foz do Iguaçu, PR'
        context['facebook'] = 'https://www.facebook.com/iasd.fozcentral'
        context['youtube'] = 'https://www.youtube.com/channel/UCsLvHS14G27MukIDiVDgiWQ'
        context['twitter'] = ''
        context['instagram'] = 'https://www.instagram.com/iasdcentralfoz2/'
        context['nome'] = 'IASD Central de Foz'
        context['telefone'] = '+55 45 99999-9999'
        context['email'] = 'email@email.com'
        return render(request, self.template_name, context)