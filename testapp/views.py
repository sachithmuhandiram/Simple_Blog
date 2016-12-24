from django.http import Http404
from django.http import HttpResponse
#from django.template import loader # replaced by render
from django.shortcuts import render
from .models import Authors #importing models
from articals.models import Articals


# Create your views here.
def index(request):
	all_authors = Authors.objects.all()		#getting all author details
	#author_template = loader.get_template('authors/author_index.html') 	#loading the view
	#creating a dictionary 
	author_data ={
		'all_authors' : all_authors,
	}
	return render(request,'authors/author_index.html',author_data) #HttpResponse(author_template.render(author_data,request)) #returning the html view
	#render function takes (request,'link to our view', data for the view)

def authors_details(request,authors_id):
	try:
		author_details=Authors.objects.get(id=authors_id)
	except Authors.DoesNotExist:
		raise Http404("That author is not availble here")
	return render(request,'authors/author_detail.html',{'author_details':author_details})
	
	



"""
if not use templetes, use this
def index(request):
	all_authors = Authors.objects.all()		#getting all author details
	html=''									#making an empty object
	for author in all_authors:
		url ='/test/' + str(author.id) +'/'		#creating url s for href
		html +='<a href="' + url + '">'+author.name+ '</a><br>' #making href
		
	return HttpResponse(html) #returning the html view
"""
	