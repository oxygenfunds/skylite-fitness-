from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    
    
    path('home/', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('index/', views.bmi, name='bmi'),

    path('trainers/', views.trainers, name='trainers'),
    
    # path('signin/', views.signin, name='signin'),
    
    path('assessment/', views.assessment, name='assessment'),
    
    path('blog/', views.blog, name='blog'),
]




# Create your URL patterns here.  