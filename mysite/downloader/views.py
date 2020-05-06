from django.shortcuts import render
from pytube import YouTube
import os.path
from django.contrib import messages



def download(request):
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method == 'POST':
        url = request.POST.get('link')
        YouTube(url).streams.filter(only_audio=True).first().download(homedir +'/Downloads')
        messages.success(request, 'video downloaded. Check your Download directory!')
    return render(request, 'download.html')

