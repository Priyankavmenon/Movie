# Generated by Django 4.2.7 on 2024-01-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_alter_movie_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='summary',
            field=models.TextField(max_length=200),
        ),
    ]
