from django.shortcuts import render
from home.views import BaseView

# Create your views here.
class AgendaView(BaseView):
    template_name = 'agenda/agenda.html'
    title = 'Agenda'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        return render(request, self.template_name, context)
