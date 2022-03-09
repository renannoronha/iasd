from .models import *
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Testemunho
from home.views import BaseView

# Create your views here.


class TestemunhosView(BaseView):
    template_name = 'testemunho/testemunhos.html'
    title = 'Testemunhos'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome

        paginator = Paginator(Testemunho.objects.all(), 10)
        page = request.GET.get('p', 1)
        try:
            testemunhos = paginator.page(page)
        except PageNotAnInteger:
            testemunhos = paginator.page(1)
        except EmptyPage:
            testemunhos = paginator.page(paginator.num_pages)

        context['testemunhos'] = testemunhos
        return render(request, self.template_name, context)


class TestemunhoView(BaseView):
    template_name = 'testemunho/testemunho.html'
    title = 'Testemunho'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome

        context['testemunho'] = Testemunho.objects.get(id=kwargs['pk'])
        return render(request, self.template_name, context)
