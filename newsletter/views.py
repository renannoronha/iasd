from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from home.views import BaseView

# Create your views here.
class NewsView(BaseView):
    template_name = 'newsletter/news.html'
    title = 'Boletins Semanais'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome

        paginator = Paginator(News.objects.all().order_by('-date'), 6)
        page = request.GET.get('p', 1)
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)

        context['news'] = news
        return render(request, self.template_name, context)


class NewsletterView(BaseView):
    template_name = 'newsletter/newsletter.html'
    title = 'Boletim Semanal'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome

        context['news'] = News.objects.get(id=kwargs['pk'])
        context['recent'] = News.objects.all().exclude(id=kwargs['pk']).order_by('-date')[:3]
        return render(request, self.template_name, context)