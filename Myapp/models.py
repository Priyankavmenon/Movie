from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    genrename=models.CharField(max_length=20)
    description=models.TextField(max_length=200)
    def __str__(self):
        return self.genrename
class Movie(models.Model):
    title=models.CharField(max_length=20)
    date=models.DateField(max_length=20)
    duration=models.CharField(max_length=20,null=True)
    summary=models.TextField(max_length=200)
    genre=models.ForeignKey(Genre,on_delete=models.PROTECT)
    image=models.ImageField(upload_to="images",null=True)
 
class Moviegenre(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    