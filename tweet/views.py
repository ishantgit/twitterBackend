from django.shortcuts import render
from tweet.serializers import *
from rest_framework.decorators import api_view
from .models import Tweet
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def get_tweets(request):
	movie = request.GET.get('movie')
	data = {}
	if not movie:
		data["message"] = "Please provide a movie id"
		return Response(data, status = status.HTTP_400_BAD_REQUEST)
	tweets = Tweet.objects.filter(movie=movie)
	serializers = TweetReadSerializer(tweets, many=True)
	data['tweets'] = serializers.data
	data['message'] = "All tweets corresponding to this movie."

	return Response(data, status = status.HTTP_400_BAD_REQUEST)
