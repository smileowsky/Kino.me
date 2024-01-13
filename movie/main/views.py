import requests, json
from datetime import datetime
from django.shortcuts import render
from . models import MovieInfo


# Create your views here.


def fetch_and_save_movies(): 
    data_from_TMDB = []
    
    data = requests.get("https://api.themoviedb.org/3/dicover/movie?api_key=43aeb22a3e8c29bf8f8c592df29550ba")
    data = json.loads(data.text)
    
    i = 0

    while i < len(data['results']):

        genre_data = requests.get('https://api.themoviedb.org/3/movie/'+str(data['results'][i]['id'])+'?api_key=43aeb22a3e8c29bf8f8c592df29550ba')
        genre_data = json.loads(data.text)

        id = data['results'][i]['id']
        title = data['results'][i]['title']
        motto = ''
        overview = data['results'][i]['overview']
        genre = genre_data['genres'][i]['name']
        director = ''
        writer = ''
        release_date = data['results'][i]['release_date']
        poster_path = data['results'][i]['poster_path']
        backdrop_path = data['result'][i]['backdrop_path']
        trailer = ''
        original_language = data['results'][i]['original_language']
        status = ''
        budget = ''
        revenue = ''
        adult = data['results'][i]['adult']
        popularity = data['results'][i]['popularity']
        vote_average = data['results'][i]['vote_average']
        vote_count = data['results'][i]['vote_count']

        check = MovieInfo.objects.filter(video_id = data['results'][i]['id']).count

        if check == 0:
            save = MovieInfo(
                m_id = id,
                m_name = title,
                m_motto = motto,
                m_description = overview,
                m_genre = genre,
                m_director = director,
                m_writer = writer,
                m_r_date = release_date,
                m_poster = poster_path,
                m_backg_im = backdrop_path,
                m_trailer = trailer,
                m_o_language = original_language,
                m_status = status,
                m_budget = budget,
                m_revenue = revenue,
                m_adult = adult,
                m_popularity = popularity,
                m_vote_average = vote_average,
                m_vote_count = vote_count
                )

    











































"""v
    api_KEY = '43aeb22a3e8c29bf8f8c592df29550ba'
    url_i = "https://api.themoviedb.org/3/discover/movie"
    url_c = "https://api.themoviedb.org/3/person/{person_id}/combined_credits"
    url_v = "https://api.themoviedb.org/3/movie/{movie_id}/videos"
    url_s = "https://api.themoviedb.org/3/list/{list_id}/item_status"

    params = {
        'api_key': api_KEY,
        'include_adult': True,
        'include_video': True,
        'language': 'en-US',
        'page': 1,
        'primary_release_date.gte': 'start_date',
        'primary_release_date.lte': 'end_date',
        'region': 'string',
        'release_date.gte': 'start_date',
        'release_date.lte': 'end_date',
        'sort_by': 'popularity.desc',
        'person_id': 'string',
        'movie_id': 'int32',
        'list_id': 'int32',

    }

    response = requests.get(url_i, url_c, url_v, url_s, params=params)
    data = response.json().get('results', [])

    for movie_data in data:
        m_name = movie_data.get('title', '')
        m_motto = movie_data.get('tagline', '')
        m_description = movie_data.get('overview', '')
        m_genre = ', '.join(genre['name'] for genre in movie_data.get('genres', []))
        m_director = movie_data.get('original_title', '')
        m_r_date = datetime.strptime(movie_data.get('release_date', ''), '%Y-%m-%d')
        m_o_language = movie_data.get('original_language', '')
        m_budget = movie_data.get('budget', 0)
        m_revenue = movie_data.get('revenue', 0)"""