from mongoengine import connect
from django.db import models

connect('mongo')

class Video(models.Model):
    identification = models.CharField("identification",max_length=100)
    titulo = models.CharField("Titulo", max_length=150)
    tema = models.CharField("Tema", max_length=100)
    url = models.CharField("URL", max_length=100)
    likes = models.IntegerField("Likes")
    deslikes = models.IntegerField("Deslikes")
    score = models.IntegerField("score")
