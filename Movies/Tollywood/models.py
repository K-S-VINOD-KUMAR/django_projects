from django.db import models

# Create your models here.
class Heroregister(models.Model):
    heroname=models.CharField(max_length=100,null=False)
    hero_age=models.IntegerField()
    hero_email=models.EmailField(max_length=30)

    def __str__(self):
        return self.heroname

class Movieregister(models.Model):
    heros=[('Maheshbabu','Maheshbabu'),('Nagarjuna','Nagarjuna')]
    movie_name=models.CharField(max_length=100)
    movie_banner=models.CharField(max_length=50)
    movie_hero=models.CharField(max_length=40)
    def __str__(self):
        return self.movie_name

class Userregister(models.Model):
    gender=[('Male','Male'),('Female','Female')]
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)
    mobile=models.IntegerField(null=False)
    password=models.CharField(max_length=20)
    usergender=models.CharField(max_length=10,choices=gender)
    def __str__(self):
        return self.email