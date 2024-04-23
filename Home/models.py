from django.db import models

# Create your models here.


class Promotion(models.Model):
    title = models.CharField(max_length=20)
    title1 = models.CharField(max_length=20)
    title2 = models.CharField(max_length=20)
    title3 = models.CharField(max_length=20)
    title4 = models.CharField(max_length=20)
    image = models.ImageField(upload_to='promote/', default='null.png')