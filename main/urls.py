from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('services/', views.services, name='Services'),
    path('gallery/', views.GalleryListView.as_view(), name='Gallery'),
    path('gallery/upload/', views.GalleryCreateView.as_view(), name='Gallery-create'),
    path('gallery/<int:pk>/delete/', views.GalleryDeleteView.as_view(), name='Gallery-delete'),
    path('testimonals/', views.testimonals, name='Testimonals'),
    path('contact/', views.contact, name='Contact'),
]