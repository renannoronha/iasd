from django.shortcuts import render
from django.db.models import F, Value, CharField, Func
from django.db.models.functions import Concat
from django.http import JsonResponse
from home.views import BaseView
from .models import *

# Create your views here.


class EscalaView(BaseView):
    template_name = 'escala/escala.html'
    title = 'Escala'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        return render(request, self.template_name, context)


class EventosView(BaseView):
    def get(self, request, *args, **kwargs):
        eventos = list(Escala.objects.all()
            .annotate(
                name=F('departamento__departamento'),
                description=F('nome'),
                date=Concat(F('data'), Value(' 00:00:00 GMT-0300'), output_field=CharField()),
                type=Concat(Value('event'), Value(''), output_field=CharField())
            )
            .values())
        return JsonResponse(eventos, safe=False)
