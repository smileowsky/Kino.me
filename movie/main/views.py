import requests
import json
from datetime import datetime
from django.shortcuts import render
from . models import MovieInfo


# Create your views here.


def fetch_and_save_movies(request):
	data_from_TMDB = []
	my_API = '43aeb22a3e8c29bf8f8c592df29550ba'
	id = ''
	imdb_id = ''
	backdrop_path = ''
	title = ''
	overview = ''
	genre = ''
	director = ''
	writer = ''
	release_date = ''
	poster_path = ''
	trailer = ''
	original_language = ''
	status = ''
	budget = ''
	revenue = ''
	adult = ''
	popularity = ''
	vote_average = ''
	vote_count = ''
	data = requests.get(
		f"https://api.themoviedb.org/3/discover/movie?api_key={my_API}")
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
			f"https://api.themoviedb.org/3/{data['results'][i]['id']}?videos?api_key={my_API}")
		movie_trailer = json.loads(movie_trailer.text)

		id = data['results'][i]['id']
		imdb_id = movie_status['imdb_id']
		title = data['results'][i]['title']
		motto = movie_status['tagline']
		overview = data['results'][i]['overview']
		genre = genre_data['genres'][i]['name']
		for crew_member in movie_data.get('crew', []):
			if crew_member.get('job') == 'Director':
				director = crew_member.get('name', '')
			elif crew_member.get('job') == 'Writer':
				writer = crew_member.get('name', '')
		release_date = data['results'][i]['release_date']
		poster_path = data['results'][i]['poster_path']
		backdrop_path = data['results'][i]['backdrop_path']

		original_language = data['results'][i]['original_language']
		status = movie_status['status']
		budget = movie_status['budget']
		revenue = movie_status['revenue']
		adult = data['results'][i]['adult']
		popularity = data['results'][i]['popularity']
		vote_average = data['results'][i]['vote_average']
		vote_count = data['results'][i]['vote_count']

		i += 1
		break

	return render(request, 'home.html', {
											'id': id,
											'imdb_id': imdb_id,
											'title': title,
											'motto': motto,
											'overview': overview,
											'genre': genre,
											'director': director,
											'writer': writer,
											'release_date': release_date,
											'poster_path': poster_path,
											'backdrop_path': backdrop_path,
											'trailer': trailer,
											'original_language': original_language,
											'status': status,
											'budget': budget,
											'revenue': revenue,
											'adult': adult,
											'popularity': popularity,
											'vote_average': vote_average,
											'vote_count': vote_count
										})


'''
			
			
			trailer = movie_trailer['results'][i]['key']

		data = MovieInfo.objects.all().order_by('-id')
	
	return render(request, 'home.html', {'ids' : ids, 'my_API' : my_API, 'data_from_TMDB' : data_from_TMDB})

	















check = MovieInfo.objects.filter(m_id=id).count()

			if check == 0:
				movie_i = MovieInfo(
					m_id = id,
					m_imdb_i = imdb_id,
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
				movie_i.save()
			i += 1
'''