import requests
import json
from datetime import datetime
from django.shortcuts import render
from django.db.models.functions import ExtractYear
from . models import MovieInfo


# Create your views here.

def home(request):
    data1 = MovieInfo.objects.all().order_by('m_popularity')[:20]
    data2 = MovieInfo.objects.values_list('m_genre', flat=True).distinct()
    data3 = MovieInfo.objects.annotate(year=ExtractYear('m_r_date')).values_list('year', flat=True).distinct().order_by('-m_r_date')
    data4 = MovieInfo.objects.all().order_by('m_r_date')[:21]

    return render(request, 'home.html', {'data1' : data1, 'data2' : data2, 'data3' : data3, 'data4' : data4})


def fetch_and_save_movies(request):

    data_from_TMDB = []
    page = 0

    if 'fetch' in request.POST:
        my_API = '43aeb22a3e8c29bf8f8c592df29550ba'

        while page < 10:
            page += 1

            data = requests.get(
                f"https://api.themoviedb.org/3/discover/movie?api_key={my_API}&page={page}")
            data = json.loads(data.text)

            i = 0

            while i < len(data['results']):

                genre_data = requests.get(
                    f"https://api.themoviedb.org/3/movie/{data['results'][i]['id']}?api_key={my_API}")
                genre_data = json.loads(genre_data.text)

                movie_data = requests.get(
                    f"https://api.themoviedb.org/3/movie/{data['results'][i]['id']}/credits?api_key={my_API}")
                movie_data = json.loads(movie_data.text)

                movie_status = requests.get(
                    f"https://api.themoviedb.org/3/movie/{data['results'][i]['id']}?api_key={my_API}")
                movie_status = json.loads(movie_status.text)

                movie_trailer = requests.get(
                    f"https://api.themoviedb.org/3/movie/{data['results'][i]['id']}/videos?api_key={my_API}")
                movie_trailer = json.loads(movie_trailer.text)

                id = data['results'][i]['id']
                imdb_id = movie_status['imdb_id']
                title = data['results'][i]['title']
                motto = movie_status['tagline']
                overview = data['results'][i]['overview']
                genres = [genre_info['name']
                          for genre_info in genre_data.get('genres', [])]
                for crew_member in movie_data.get('crew', []):
                    if crew_member.get('job') == 'Director':
                        director = crew_member.get('name', '')
                    elif crew_member.get('job') == 'Writer':
                        writer = crew_member.get('name', '')
                release_date = data['results'][i]['release_date']
                poster_path = data['results'][i]['poster_path']
                backdrop_path = data['results'][i]['backdrop_path']
                for trailer_info in movie_trailer.get('results', []):
                    if 'trailer' in trailer_info.get('name', '').lower():
                        if trailer_info != '':
                            trailer = trailer_info['key']
                        else:
                            trailer_info = ''
                original_language = data['results'][i]['original_language']
                status = movie_status['status']
                if movie_status['budget'] != 0 and movie_status['budget'] != '-':
                    budget = movie_status['budget']
                    revenue = movie_status['revenue']
                else:
                    budget = 0
                    revenue = 0
                adult = data['results'][i]['adult']
                try:
                    popularity = data['results'][i]['popularity']
                    vote_average = data['results'][i]['vote_average']
                except TypeError:
                    popularity = 0
                    vote_average = 0
                vote_count = data['results'][i]['vote_count']

                check = MovieInfo.objects.filter(m_id=id).count()

                if check == 0:
                    movie_i = MovieInfo(
                        m_id=id,
                        m_imdb_i=imdb_id,
                        m_name=title,
                        m_motto=motto,
                        m_description=overview,
                        m_genre=', '.join(genres),
                        m_director=director,
                        m_writer=writer,
                        m_r_date=release_date,
                        m_poster=poster_path,
                        m_backg_im=backdrop_path,
                        m_trailer=trailer,
                        m_o_language=original_language,
                        m_status=status,
                        m_budget=budget,
                        m_revenue=revenue,
                        m_adult=adult,
                        m_popularity=popularity,
                        m_vote_average=vote_average,
                        m_vote_count=vote_count
                    )
                    movie_i.save()
                i += 1

    data = MovieInfo.objects.all().order_by('-id')

    return render(request, 'movie.html', {'data_from_TMDB' : data_from_TMDB, 'data': data})
