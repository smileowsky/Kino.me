# Generated by Django 4.2.4 on 2024-01-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='m_genre',
            field=models.CharField(max_length=255),
        ),
    ]
