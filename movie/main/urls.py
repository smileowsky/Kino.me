from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie', views.fetch_and_save_movies, name='movie'),
    path('series', views.fetch_and_save_series, name='series'),
    path('signin', views.login, name='signin'),
    path('signup', views.registration, name='signup'),
]
