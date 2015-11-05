from django.db import models
from movie.models import Movie

# Create your models here.

class Tweet(models.Model):
	movie = models.ForeignKey(Movie, null = True)
	text = models.TextField(null = True ,blank = True) 
	polarity = models.DecimalField(null = True,blank = True, decimal_places = 20 , max_digits = 25)
	subjectivity = models.DecimalField(null = True,blank = True, decimal_places = 20 , max_digits = 25)
