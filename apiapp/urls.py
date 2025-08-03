from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
]
