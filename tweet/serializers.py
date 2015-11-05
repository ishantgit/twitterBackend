from rest_framework import serializers
from tweet.models import *

class TweetCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tweet

class TweetReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tweet
		depth = 2
