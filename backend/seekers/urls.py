from django.urls import path
from . import views

urlpatterns=[
  path('', views.index, name='index'),
  path('upload_cv/', views.upload_cv, name ='upload_cv'),
  path('submit_pitch/', views.submit_pitch, name ='submit_pitch'),
  path('profile/', views.profile, name='profile'),
  path('cv/<str:pk>/', views.cv_details, name='cv_details'),
  path('rate_cv/<str:pk>', views.rate_cv, name = 'rate_cv'),
  path('pitch/', views.pitch, name='pitch'),
  path('pitch/<str:pk>/', views.pitch_details, name='pitch_details'),
  path('pitch/<str:pk>/comment', views.comment, name = 'comment'),
]