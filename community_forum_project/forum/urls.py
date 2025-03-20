from django.urls import path
from .views import register, login, logout, ProfileView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]