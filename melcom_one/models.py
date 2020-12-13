from django.db import models

# Creating my video database 

class Video(models.Model):
    id = models.AutoField(default=1,primary_key=True)
    name = models.CharField(max_length=500)
    # videofile = models.FileField(upload_to='video/',null=True,verbose_name="")
    
    def __str__(self):
        return self.name 
