from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import MyTokenObtainPairView, RegisterView, LoginView



urlpatterns = [
    path('', views.get_routes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('resume/', views.get_resume),
    path('add_resume/', views.add_resume),
    # path('pitch/', views.get_pitch),
    # path('add_pitch/', views.add_pitch),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    
]
