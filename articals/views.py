from django.http import Http404
from django.http import HttpResponse
#from django.template import loader # replaced by render
from django.shortcuts import render
from .models import Articals #importing models
from testapp.models import Authors #importing models

# Create your views here.
def articals_details(request,artical_title):
	try:
		artical_details = Articals.objects.get(artical_title=artical_title)
	except Articals.DoesNotExist:
		raise Http404("That Artical is not availble here")
	return render(request,'articals/artical_index.html',{'artical_details':artical_details})