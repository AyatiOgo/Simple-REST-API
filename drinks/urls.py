from django.urls import path
from .views import get_drinks, drink_info

urlpatterns = [
    path('drinks/', get_drinks, name='get_drinks'),
    path('drink/<int:pk>/', drink_info, name='drink_info'),

]
