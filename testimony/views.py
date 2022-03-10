from .models import *
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Testimony
from home.views import BaseView

# Create your views here.


class TestimoniesView(BaseView):
    template_name = 'testimony/testimonies.html'
    title = 'Testemunhos'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome

        paginator = Paginator(Testimony.objects.all(), 10)
        page = request.GET.get('p', 1)
        try:
            testimonies = paginator.page(page)
        except PageNotAnInteger:
            testimonies = paginator.page(1)
        except EmptyPage:
            testimonies = paginator.page(paginator.num_pages)

        context['testimonies'] = testimonies
        return render(request, self.template_name, context)


class TestimonyView(BaseView):
    template_name = 'testimony/testimony.html'
    title = 'Testemunho'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome

        context['testimony'] = Testimony.objects.get(id=kwargs['pk'])
        return render(request, self.template_name, context)
