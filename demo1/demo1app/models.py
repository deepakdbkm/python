from django.db import models

# Create your models here.
class place (models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
    non=models.TextField()


    def __str__(self):
        return self.name
class place1(models.Model):
    name1=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc1=models.TextField()
    def __str__(self):
     return self.name1