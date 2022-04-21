from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('', views.get_routes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('resume/', views.get_resume),
    path('add_resume/', views.add_resume),
    path('pitch/', views.get_pitch),
    path('add_pitch/', views.add_pitch),
    
]
