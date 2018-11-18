from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Club(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	members = models.ManyToManyField(User)

class Announcement(models.Model):
	club = models.ForeignKey(Club, on_delete=models.CASCADE)
	text = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
