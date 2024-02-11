# Generated by Django 4.2.4 on 2024-02-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CastInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_director', models.CharField(max_length=25)),
                ('m_writer', models.CharField(max_length=25)),
                ('m_actors', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GenreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_genre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.BigIntegerField()),
                ('m_imdb_i', models.CharField(blank=True, max_length=20, null=True)),
                ('m_name', models.CharField(max_length=100)),
                ('m_motto', models.CharField(max_length=200)),
                ('m_r_date', models.DateField()),
                ('m_description', models.TextField()),
                ('m_poster', models.CharField(max_length=255)),
                ('m_backg_im', models.CharField(max_length=255)),
                ('m_trailer', models.CharField(blank=True, max_length=50, null=True)),
                ('m_o_language', models.CharField(max_length=30)),
                ('m_status', models.CharField(default=True, max_length=20)),
                ('m_budget', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('m_revenue', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('m_adult', models.CharField(default=False, max_length=10)),
                ('m_popularity', models.IntegerField()),
                ('m_vote_average', models.IntegerField()),
                ('m_vote_count', models.IntegerField()),
                ('m_cast', models.ManyToManyField(related_name='movies', to='main.castinfo')),
                ('m_genres', models.ManyToManyField(related_name='movies', to='main.genreinfo')),
            ],
        ),
    ]