from django.db import models

# Create your models here.

class Movie(models.Model):
	name = models.CharField(unique = True, max_length = 100)
	genre = models.CharField(null = True ,max_length = 200)
	langage = models.CharField(null = True, max_length = 200)
	imdbRating = models.CharField(null = True, max_length = 200)
	plot = models.TextField(null = True)
	actor = models.CharField(null = True, max_length = 200)
	writer = models.CharField(null = True, max_length = 200)
	director = models.CharField(null = True, max_length = 200)
	poster = models.CharField(null = True,max_length = 200)

	def __str__(self):
		return self.name
