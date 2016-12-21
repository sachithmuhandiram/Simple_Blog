from django.http import HttpResponse
from django.template import loader #
from .models import Authors #importing models


# Create your views here.
def index(request):
	all_authors = Authors.objects.all()		#getting all author details
	author_template = loader.get_template('authors/author_index.html') 	#loading the view
	#creating a dictionary
	author_data ={
		'all_authors' : all_authors,
	}
	return HttpResponse(author_template.render(author_data,request)) #returning the html view

def authors_details(request,authors_id):
	return HttpResponse("<h1>Author ID is : "+str(authors_id)+"</h2>")



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
	