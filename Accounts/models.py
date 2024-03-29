from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Customusers(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', default='def.png')
    email = models.EmailField(max_length=40, unique=True)
    otp = models.CharField(max_length=5)
    is_verified = models.BooleanField(default=False)


def __str__(self):
    return self.username  


class address(models.Model):
    user = models.ForeignKey(Customusers, on_delete=models.CASCADE)
    title = models.TextField(max_length=50, blank = False, null = False)
    house = models.TextField(max_length=60, blank = False, null = False)
    road = models.TextField(max_length=255, blank = False, null = False)
    thana = models.TextField(max_length=255, blank = False, null = False)
    postoffice = models.TextField(max_length=255, blank = False, null = False)
    town = models.TextField(max_length=255, blank = False, null = False)
    phone = models.TextField(max_length=17, blank = True, null = True, )

def __str__(self):
    return self.user.username
