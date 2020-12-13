from django.shortcuts import render
from .models import Video
from django.conf import settings
import os


def index(request):
    path = settings.MEDIA_ROOT
    media = os.listdir(path + '/')
    context = {'media' : media,'name':media}
    return render(request, 'melcom_one/index.html', context)


def sortvideo(request):
    if request.method =="GET":
        query = request.GET['mel']
        return render(request,'melcom_one/index.html',{'sort':query})
        