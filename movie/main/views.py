import requests
import json
from django.shortcuts import render
from django.db.models import Q
from . models import MovieInfo, GenreInfo, CastInfo, TVSeriesInfo, TVGenreInfo, TVCastInfo


# Create your views here.
def home(request):
    new_release = MovieInfo.objects.all().order_by('-m_r_date')[:5]
    movie_list = MovieInfo.objects.all().order_by('-m_popularity')[:30]
    movie_vote = MovieInfo.objects.all().order_by('-m_vote_average')[:18]
    trailers = MovieInfo.objects.all().order_by('-m_r_date')[:18]
    return render(request, 'home.html', {'new_release' : new_release, 'movie_list' : movie_list, 'movie_vote' : movie_vote, 'trailers' : trailers})


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
                actors = []
                for cast_info in movie_data.get('cast', []):
                    actors.append(cast_info['name'])
                    if len(actors) == 5:
                        break
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
                if adult == False:
                    adult = 'False'
                else:
                    adult = 'True'
                try:
                    popularity = data['results'][i]['popularity']
                    vote_average = data['results'][i]['vote_average']
                except TypeError:
                    popularity = 0
                    vote_average = 0
                vote_count = data['results'][i]['vote_count']
                runtime = movie_status['runtime']
                if movie_status['runtime'] != 0 and movie_status['runtime'] != '-':
                    runtime = movie_status['runtime']
                else:
                    runtime = 0

                check = MovieInfo.objects.filter(m_id=id).count()

                if check == 0:
                    genres_objects = []
                    for genre_name in genres:
                        genre, _ = GenreInfo.objects.get_or_create(
                            m_genre=genre_name)
                        genres_objects.append(genre)

                    actors_objects = []
                    for actor_name in actors:
                        actor, _ = CastInfo.objects.get_or_create(
                            m_actors=actor_name)
                        actors_objects.append(actor)

                    movie_i = MovieInfo.objects.create(
                        m_id=id,
                        m_imdb_i=imdb_id,
                        m_name=title,
                        m_motto=motto,
                        m_description=overview,
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
                        m_vote_count=vote_count,
                        m_runtime=runtime,

                    )
                    movie_i.m_genres.set(genres_objects)

                    cast_info, _ = CastInfo.objects.get_or_create(
                        m_director=director,
                        m_writer=writer,
                    )
                    movie_i.m_cast.add(cast_info)

                i += 1

    if 'delete_all' in request.POST:
        MovieInfo.objects.all().delete()
        CastInfo.objects.all().delete()
        GenreInfo.objects.all().delete()

    if 'question' in request.POST:
        data = MovieInfo.objects.filter(
            Q(m_name__contains=request.POST['question']) | Q(m_genres__contains=request.POST['question'] | Q(m_status__contains=request.POST['question']))).order_by('-id')
    else:
        data = MovieInfo.objects.all().order_by('-id')

    return render(request, 'movie.html', {'data_from_TMDB': data_from_TMDB, 'data': data,})


def fetch_and_save_series(request):

    data_from_TMDB = []
    page = 0

    if 'fetch' in request.POST:
        my_API = '43aeb22a3e8c29bf8f8c592df29550ba'

        while page < 10:
            page += 1

            data = requests.get(
                f"https://api.themoviedb.org/3/discover/tv?api_key={my_API}&page={page}")
            data = json.loads(data.text)

            i = 0

            while i < len(data['results']):

                genre_data = requests.get(
                    f"https://api.themoviedb.org/3/tv/{data['results'][i]['id']}?api_key={my_API}")
                genre_data = json.loads(genre_data.text)

                series_data = requests.get(
                    f"https://api.themoviedb.org/3/tv/{data['results'][i]['id']}/credits?api_key={my_API}")
                series_data = json.loads(series_data.text)

                series_status = requests.get(
                    f"https://api.themoviedb.org/3/tv/{data['results'][i]['id']}?api_key={my_API}")
                series_status = json.loads(series_status.text)

                series_trailer = requests.get(
                    f"https://api.themoviedb.org/3/tv/{data['results'][i]['id']}/videos?api_key={my_API}")
                series_trailer = json.loads(series_trailer.text)

                id = data['results'][i]['id']
                try:
                    num_season = series_status['last_episode_to_air'][i]['season_number']
                except KeyError:
                    num_season = 0
                title = data['results'][i]['original_name']
                motto = series_status['tagline']
                overview = data['results'][i]['overview']
                genres = [genre_info['name']for genre_info in genre_data.get('genres', [])]
                created_by = []
                for crew_member in series_data.get('created_by', []):
                    created_by.append(crew_member['name'])
                    if len(created_by) == 2:
                        break
                actors = []
                for cast_member in series_data.get('cast', []):
                    actors.append(cast_member['name'])
                    if len(actors) == 5:
                        break
                first_air_date = data['results'][i]['first_air_date']
                if 'last_air_date' in data:
                    last_air_date = series_data['last_air_date']
                else:
                    last_air_date = None
                poster_path = data['results'][i]['poster_path']
                bacdrop_path = data['results'][i]['backdrop_path']
                trailer = []
                for trailer_info in series_trailer.get('results', []):
                    if 'type' in trailer_info and trailer_info['type'] == 'Trailer':
                        trailer = trailer_info['key']
                        if len(trailer) == 1:
                            break
                original_language = series_status['original_language']
                status = series_status['status']
                adult = series_status['adult']
                if adult == False:
                    adult = 'False'
                else:
                    adult = 'True'
                try:
                    popularity = data['results'][i]['popularity']
                    vote_average = data['results'][i]['vote_average']
                except TypeError:
                    popularity = 0
                    vote_average = 0
                vote_count = data['results'][i]['vote_count']

                check = TVSeriesInfo.objects.filter(tv_id=id).count()

                if check == 0:
                    genres_objects = []
                    for genre_name in genres:
                        genre, _ = TVGenreInfo.objects.get_or_create(
                            tv_genre=genre_name)
                        genres_objects.append(genre)
                    
                    actors_objects = []
                    for actor_name in actors:
                        actor, _ = TVCastInfo.objects.get_or_create(
                            tv_actors=actor_name)
                        actors_objects.append(actor)

                    series_i = TVSeriesInfo.objects.create(
                        tv_id=id,
                        tv_season_number=num_season,
                        tv_name=title,
                        tv_motto=motto,
                        tv_r_date=first_air_date,
                        tv_e_date=last_air_date,
                        tv_description=overview,
                        tv_poster=poster_path,
                        tv_backg_im=bacdrop_path,
                        tv_trailer=trailer,
                        tv_o_language=original_language,
                        tv_status=status,
                        tv_adult=adult,
                        tv_popularity=popularity,
                        tv_vote_average=vote_average,
                        tv_vote_count=vote_count
                    )
                    series_i.tv_genres.set(genres_objects)

                    cast_info, _ = TVCastInfo.objects.get_or_create(
                        tv_creator=created_by
                    )
                    series_i.tv_cast.add(cast_info)
                
                i += 1
    
    if 'delete_all' in request.POST:
        TVSeriesInfo.objects.all().delete()
        TVCastInfo.objects.all().delete()
        TVGenreInfo.objects.all().delete()

    if 'question' in request.POST:
        data = TVSeriesInfo.objects.filter(
            Q(tv_name__contains=request.POST['question'])
        )
    else:
        data = TVSeriesInfo.objects.all().order_by('-id')
    
    return render(request, 'tv_series.html', {'data_from_TMDB' : data_from_TMDB, 'data' : data})