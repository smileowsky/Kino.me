from django.db import models

# Create your models here.


class MovieInfo(models.Model):
    m_id = models.BigIntegerField()
    m_imdb_i = models.CharField(max_length=20, blank=True, null=True)
    m_name = models.CharField(max_length=100)
    m_motto = models.CharField(max_length=200)
    m_r_date = models.DateField()
    m_description = models.TextField()
    m_genres = models.ManyToManyField('GenreInfo', related_name='movies')
    m_cast = models.ManyToManyField('CastInfo', related_name='movies')
    m_poster = models.CharField(max_length=255)
    m_backg_im = models.CharField(max_length=255)
    m_trailer = models.CharField(max_length=50, blank=True, null=True)
    m_o_language = models.CharField(max_length=30)
    m_status = models.CharField(max_length=20, default=True)
    m_budget = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    m_revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    m_adult = models.CharField(max_length=10, default=False)
    m_popularity = models.IntegerField()
    m_vote_average = models.IntegerField()
    m_vote_count = models.IntegerField()
    m_runtime = models.IntegerField()

class GenreInfo(models.Model):
    m_genre = models.CharField(max_length=255)

class CastInfo(models.Model):
    m_director = models.CharField(max_length=25)
    m_writer = models.CharField(max_length=25)
    m_actors = models.CharField(max_length=30)

class TVSeriesInfo(models.Model):
    tv_id = models.BigIntegerField()
    tv_season_number = models.CharField(max_length=20, blank=True, null=True)
    tv_name = models.CharField(max_length=100)
    tv_motto = models.CharField(max_length=200)
    tv_r_date = models.DateField()
    tv_e_date = models.DateField()
    tv_description = models.TextField()
    tv_genres = models.ManyToManyField('TVGenreInfo', related_name='tvseries')
    tv_cast = models.ManyToManyField('TVCastInfo', related_name='tvseries')
    tv_poster = models.CharField(max_length=255)
    tv_backg_im = models.CharField(max_length=255)
    tv_trailer = models.CharField(max_length=50, blank=True, null=True)
    tv_o_language = models.CharField(max_length=30)
    tv_status = models.CharField(max_length=20, default=True)
    tv_adult = models.CharField(max_length=10, default=False)
    tv_popularity = models.IntegerField()
    tv_vote_average = models.IntegerField()
    tv_vote_count = models.IntegerField()

class TVGenreInfo(models.Model):
    tv_genre = models.CharField(max_length=255)

class TVCastInfo(models.Model):
    tv_creator = models.CharField(max_length=25)
    tv_actors = models.CharField(max_length=30)