from __future__ import unicode_literals

from django.db import models
import testapp

# Create your models here.
class Articals(models.Model):
	author = models.ForeignKey('testapp.models.Authors')
	artical_title = models.CharField(max_length=50)               
	artical = models.CharField(max_length=1000)