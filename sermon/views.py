from .models import *
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Sermon
from home.views import BaseView

from apiclient.discovery import build
from datetime import datetime
import requests
import os

# Create your views here.
def getNewVideos():
    try:
        api_key = open(os.path.join(settings.BASE_DIR, "api_key.txt"), "r").read()
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = 'UCsLvHS14G27MukIDiVDgiWQ'

        response = youtube.channels().list(id=channel_id, part='contentDetails').execute()
        playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        response = youtube.playlistItems().list(playlistId=playlist_id, part='snippet').execute()

        lastVideo = Sermon.objects.all().order_by('-date').first()
        for video in response['items']:
            date = datetime.strptime(video['snippet']['publishedAt'][:-1], '%Y-%m-%dT%H:%M:%S').date()
            if date == lastVideo.date:
                print(date)
                print(lastVideo.date)
                break
            elif date > lastVideo.date:
                try:
                    img_data = requests.get(video['snippet']['thumbnails']['maxres']['url']).content
                except Exception as e:
                    img_data = requests.get(video['snippet']['thumbnails']['high']['url']).content
                file_path = 'sermon/' + video['snippet']['resourceId']['videoId'] + '.jpg'
                with open(os.path.join(settings.BASE_DIR, 'media/' + file_path), 'wb') as handler:
                    handler.write(img_data)

                title = video['snippet']['title'].split(' - ')[0]
                speaker = video['snippet']['title'].split(' - ')[1] if ' - ' in video['snippet']['title'] else 'Placeholder'
                Sermon.objects.create(
                    thumbnail=file_path,
                    title=title,
                    speaker=speaker,
                    date=date,
                    description=video['snippet']['description'],
                    link='https://www.youtube.com/watch?v=' + video['snippet']['resourceId']['videoId'],
                    ativo=False,
                )
    except Exception as e:
        print(e)

class SermonsView(BaseView):
    template_name = 'sermon/sermons.html'
    title = 'Sermões'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        
        paginator = Paginator(Sermon.objects.all().order_by('-date'), 10)
        page = request.GET.get('p', 1)
        try:
            sermons = paginator.page(page)
        except PageNotAnInteger:
            sermons = paginator.page(1)
        except EmptyPage:
            sermons = paginator.page(paginator.num_pages)

        context['sermons'] = sermons
        return render(request, self.template_name, context)

class SermonView(BaseView):
    template_name = 'sermon/sermon.html'
    title = 'Sermão'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        
        context['sermon'] = Sermon.objects.get(id=kwargs['pk'])
        context['sermon'].link = context['sermon'].link.replace('watch?v=', 'embed/')
        context['sermons'] = Sermon.objects.filter(ativo=True).exclude(id=kwargs['pk']).order_by('-date')[:3]
        return render(request, self.template_name, context)
