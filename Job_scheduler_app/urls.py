from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.create_interview, name='create_interview'),  
    path('home/', views.home, name='home'), 
]