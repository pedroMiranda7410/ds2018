from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

def __str__(self):
  return self.user.username

class Usuario(models.Model):

	nome = models.CharField(max_length = 35)

	conhecimento_java = models.BooleanField()

	conhecimento_python = models.BooleanField()

	conhecimento_aeromodelismo = models.BooleanField()

	conhecimento_fenomenos = models.BooleanField()

	id = models.IntegerField(primary_key = True)