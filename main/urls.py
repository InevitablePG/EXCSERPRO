from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('services/', views.services, name='Services'),
    path('gallery/', views.gallery, name='Gallery'),
    path('testimonals/', views.testimonals, name='Testimonals'),
    path('contact/', views.contact, name='Contact'),
]