from django.urls import path
from . import views

# from django import settings 
# from django.conf import settings

# urlpatterns = [
#     path('', views.home, name='home'),
#     # path('bmi', views.bmi, name='bmi' ),
    
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
    
#    path('index/',views.bmi, name='index'),
   
#    path('home', views.home, name='home'),
  
#      path('trainers/', views.trainers, name='trainers'),
     
     
# ]

urlpatterns = [
    path('', views.home, name='home'),
    
    
    path('home/', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('index/', views.bmi, name='bmi'),

    path('trainers/', views.trainers, name='trainers'),
]




# Create your URL patterns here.  