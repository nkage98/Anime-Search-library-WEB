from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('anime/<anime_id>', views.anime_info, name="anime_info"), 
]