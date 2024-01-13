from django.db import models

# Create your models here.


class MovieInfo(models.Model):
    m_id = models.BigIntegerField()
    m_name = models.CharField(max_length=100)
    m_motto = models.CharField(max_length=200)
    m_description = models.TextField()
    m_genre = models.CharField(max_length=10)
    m_director = models.CharField(max_length=25)
    m_writer = models.CharField(max_length=25)
    m_r_date = models.DateTimeField()
    m_poster = models.ImageField(
        upload_to='media/m_poster/', blank=True, null=True)
    m_backg_im = models.ImageField(
        upload_to='media/m_bacground_image/', blank=True, null=True)
    m_trailer = models.URLField()
    m_o_language = models.CharField(max_length=30)
    m_status = models.CharField(max_length=20)
    m_budget = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    m_revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    m_adult = models.CharField(max_length=10, default=False)
    m_popularity = models.FloatField(default=0.0),
    m_vote_average = models.FloatField(default=0.0),
    m_vote_count = models.FloatField(default=0.0)