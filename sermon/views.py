from django.shortcuts import render
from django.conf import settings
from .models import Sermon

from apiclient.discovery import build
from datetime import datetime
import requests
import os

# Create your views here.
def getNewVideos():
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
            img_data = requests.get(video['snippet']['thumbnails']['maxres']['url']).content
            file_path = 'sermon/' + video['snippet']['resourceId']['videoId'] + '.jpg'
            with open('media/' + file_path, 'wb') as handler:
                handler.write(img_data)

            speaker = video['snippet']['title'].split(' - ')[1] if ' - ' in video['snippet']['title'] else 'Placeholder'
            Sermon.objects.create(
                thumbnail=file_path,
                title=video['snippet']['title'],
                speaker=speaker,
                date=date,
                description=video['snippet']['description'],
                link='https://www.youtube.com/watch?v=' + video['snippet']['resourceId']['videoId'],
                ativo=False,
            )