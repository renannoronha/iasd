from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from home.views import BaseView
from .models import Ministry

# Create your views here.
class MinistriesView(BaseView):
    template_name = 'ministries/ministries.html'
    title = 'Ministérios'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome

        paginator = Paginator(Ministry.objects.all(), 6)
        page = request.GET.get('p', 1)
        try:
            ministries = paginator.page(page)
        except PageNotAnInteger:
            ministries = paginator.page(1)
        except EmptyPage:
            ministries = paginator.page(paginator.num_pages)

        context['ministries'] = ministries
        return render(request, self.template_name, context)
