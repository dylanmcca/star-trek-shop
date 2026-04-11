from django.urls import path
from .views import quotes_list

urlpatterns = [
    path('', quotes_list, name='quotes'),
]
