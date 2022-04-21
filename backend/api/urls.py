from django.urls import path
from . import views


urlpatterns = [
    path('resume/', views.get_resume),
    path('add_resume/', views.add_resume),
    path('pitch/', views.get_pitch),
    path('add_pitch/', views.add_pitch),
    
]
