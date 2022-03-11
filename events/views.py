from django.shortcuts import render

from .models import Events

from home.views import BaseView

from datetime import datetime

# Create your views here.
class EventsView(BaseView):
    template_name = 'events/events.html'
    title = 'Eventos'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        context['events'] = Events.objects.filter(endTime__gte=datetime.now()).order_by('startTime')
        return render(request, self.template_name, context)

class EventosView(BaseView):
    def get(self, request, *args, **kwargs):
        eventos = list(Events.objects.all()
            .annotate(
                name=F('departamento__departamento'),
                description=F('nome'),
                date=Concat(F('data'), Value(' 00:00:00 GMT-0300'), output_field=CharField()),
                type=Concat(Value('event'), Value(''), output_field=CharField())
            )
            .values())
        return JsonResponse(eventos, safe=False)

class EventView(BaseView):
    template_name = 'events/event.html'
    title = 'Evento'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        
        context['event'] = Events.objects.get(id=kwargs['pk'])
        context['events'] = Events.objects.filter().exclude(id=kwargs['pk']).order_by('startTime')[:3]
        return render(request, self.template_name, context)
