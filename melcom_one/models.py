from os import name
from django.db import models

# Creating my video database 

class BackEndThings(models.Model):
    channel_name = models.CharField(max_length=100)
    source_folder = models.CharField(max_length=100)
    old_file_format = models.CharField(max_length=6)
    new_file_format = models.CharField(max_length=6)
    
    def __str__(self):
        return self.channel_name

class DataBaseUPdate(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
