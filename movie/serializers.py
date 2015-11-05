from rest_framework import serializers
from movie.models import *

class MovieCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie

class MovieReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		depth = 2
