from __future__ import unicode_literals

from django.db import models

#Articlas
class Authors(models.Model):
	name = models.CharField(max_length=250)
	email = models.CharField(max_length=50)
	telephone = models.CharField(max_length=15)

	def __str__(self):
		return self.name + ' - ' + self.email

	
class Articals(models.Model):
	author = models.ForeignKey(Authors,on_delete=models.CASCADE)
	artical_title = models.CharField(max_length=50)               
	artical = models.CharField(max_length=1000)
	


