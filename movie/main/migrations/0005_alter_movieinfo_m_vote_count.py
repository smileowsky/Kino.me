# Generated by Django 4.2.4 on 2024-01-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_movieinfo_m_imdb_i_alter_movieinfo_m_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='m_vote_count',
            field=models.IntegerField(),
        ),
    ]