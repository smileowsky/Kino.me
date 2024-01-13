from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_and_save_movies, name='fetch_and_save_movies')
]
