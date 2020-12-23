from django.conf import settings
from melcom_one.models import DataBaseUPdate
settings.configure()
import os

def update_db():
    path = settings.configure()
    media = os.listdir(path + '/')
    if media:
        for file in media:
            c = DataBaseUPdate.objects.create(name=file)
            c.save()
            