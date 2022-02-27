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
    template_name = ''
    title = 'Página Inicial - IASD Central de Foz'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title
        context['endereco'] = self.title
        context['facebook'] = self.title
        context['twitter'] = self.title
        context['instagram'] = self.title
        context['nome'] = self.title
        return render(request, self.template_name, context)