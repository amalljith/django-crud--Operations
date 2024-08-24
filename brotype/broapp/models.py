from django.db import models

# Create your models here.
class De(models.Model):
    name=models.CharField(max_length=50,)
    place=models.CharField(max_length=100)
    position=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField()
    mobile = models.CharField(max_length=100)
    