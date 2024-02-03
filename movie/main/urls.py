from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie', views.fetch_and_save_movies, name='movie')
]
