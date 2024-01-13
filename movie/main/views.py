from django.shortcuts import render
import requests, json

# Create your views here.


def movie_info(request):

    movie_data = []
    api_KEY = '43aeb22a3e8c29bf8f8c592df29550ba'
    data = request.get('https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=true&language=en-US&page=1&primary_release_date.gte=date&primary_release_date.lte=date&region=string&release_date.gte=date&release_date.lte=date&sort_by=popularity.desc')
    data = json.loads(data.text)
    
    i = 0

    while i < len(data['results']):
        name = data['results'][i]['title']
        motto = data
        description = data
        genre = data
        director = data
        writer = data
        release = data
        poster = data
        background = data
        trailer = data
        language = data
        satatus = data
        budget = data
        revenue = data
        
        i += 1

    return render(request, 'home.html', {'titles': titles, 'years': years, 'title_search': title_search, 'f_years_search': f_years_search, 't_years_search': t_years_search})