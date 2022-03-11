from django.shortcuts import render

from .models import Gallery

from home.views import BaseView

# Create your views here.
class HomeView(BaseView):
    template_name = 'gallery/gallery.html'
    title = 'Galeria de Fotos'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        context['gallery'] = Gallery.objects.filter(ativo=True)
        return render(request, self.template_name, context)