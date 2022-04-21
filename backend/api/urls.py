from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_resume),
    path('add/', views.add_resume),
]
