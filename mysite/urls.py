from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('travel', views.travel, name='travel'),
    path('travelgallery/<slug:topic_name>/', views.travelgallery, name='travelGallery'),
    path('traveldetails/<slug:topic_name>/<int:photo_id>', views.traveldetails, name='travelDetails'),
    path('projectdescription/<slug:project_name>/', views.projectdescription, name='projectDescription'),
]
