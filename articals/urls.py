from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.artical_index,name='artical_index'), 
    #url(r'^(?P<articals_title>[0-9]+)/$',views.articals_details, name="articals_details"),
    
    
]