from django.urls import path
from . import views

urlpatterns = [
    path('movie', views.fetch_and_save_movies, name='movie'),
    path('', views.home, name='home'),
]
