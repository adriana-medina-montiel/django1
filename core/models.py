from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=30)
    description= models.TextField(max_length=255)
    url=models.URLField()
    image = models.FileField(upload_to='uploads/')
# Create your models here.
