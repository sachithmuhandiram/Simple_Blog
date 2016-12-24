from __future__ import unicode_literals

from django.db import models
import articals

class Authors(models.Model):
	name = models.CharField(max_length=250)
	email = models.CharField(max_length=50)
	telephone = models.CharField(max_length=15)

	def __str__(self):			#this function belongs to Authors
		return self.name + ' - ' + self.email

class Comments(models.Model):
	comment = models.CharField(max_length=250)
	commentor = models.ForeignKey(Authors,on_delete=models.CASCADE)
	artical_id = models.ForeignKey('articals_id.Articals')



	

	
		
	


