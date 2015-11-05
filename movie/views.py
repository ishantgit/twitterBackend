from django.shortcuts import render
from movie.serializers import *
from rest_framework.decorators import api_view
from .models import Movie
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def get_movies(request):
	movie = Movie.objects.all()
	movie.reverse()
	data = {}
	serializer = MovieReadSerializer(movie, many=True)
	data['message'] = "list of movies latest first"
	data['movies'] = serializer.data
	return Response(data, status = status.HTTP_200_OK)
