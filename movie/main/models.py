from django.db import models

# Create your models here.


class MovieInfo(models.Model):
    m_name = models.CharField(max_length=100)
    m_motto = models.CharField(max_length=200)
    m_description = models.TextField()
    m_genre = models.CharField(max_length=100)
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
    m_budget = models.IntegerField(max_length=50)
    m_revenue = models.IntegerField(max_length=50)
