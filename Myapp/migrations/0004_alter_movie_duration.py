# Generated by Django 4.2.7 on 2024-01-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_alter_genre_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
