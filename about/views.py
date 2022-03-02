from django.shortcuts import render
from home.views import BaseView

# Create your views here.
class AboutView(BaseView):
    template_name = 'about/about.html'
    title = 'Sobre'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        return render(request, self.template_name, context)