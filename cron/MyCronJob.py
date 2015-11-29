"""
create database twitter;
use twitter;
create table movie(
id bigint(20) not null auto_increment primary key,
tweet text,
created_at varchar(40) ,
username text ,
favourite_count varchar(40), 
place text, 
hashtags text, 
urls text,
movie_name text
);


Sample JSON:
{"movie_info": {"username": "sreeku9999", "movie_name": "Rudhramadevi", "created_at": "Tue Oct 13 05:08:56 +0000 2015", "hashtags": ["BruceLeeTheFighter"], "place": null, "urls": [], "favourites": 0, "tweet": "Movie Rudhramadevi which has changed it's release date nearly 10 times..Now blaming #BruceLeeTheFighter ..is a sheer comedy i say"}}
{"movie_info": {"username": "Elbert_Reyner", "movie_name": "Pan", "created_at": "Tue Oct 13 05:08:57 +0000 2015", "hashtags": ["Pan"], "place": null, "urls": ["bit.ly/1LIrYuI"], "favourites": 0, "tweet": "RT @Variety: Does #Pan's box office bomb spell the end for origin movies? http://t.co/POEjfkALSt http://t.co/9qIm1cOEzp"}}
{"movie_info": {"username": "Malaa3d", "movie_name": "pan", "created_at": "Tue Oct 13 05:09:04 +0000 2015", "hashtags": [], "place": null, "urls": [], "favourites": 0, "tweet": "RT @danielsahyounie: Great work on pan... You killed it man :) Aussie pride :) @levizanemiller"}}
{"movie_info": {"username": "OhNoIAmLost", "movie_name": "pan", "created_at": "Tue Oct 13 05:09:04 +0000 2015", "hashtags": [], "place": null, "urls": [], "favourites": 0, "tweet": "RT @danielsahyounie: Great work on pan... You killed it man :) Aussie pride :) @levizanemiller"}}
{"movie_info": {"username": "Coach_Miles_", "movie_name": "pan", "created_at": "Tue Oct 13 05:09:08 +0000 2015", "hashtags": [], "place": null, "urls": [], "favourites": 0, "tweet": "RT @lilEfromthepaxk: if only my rapping career would pan out already."}}

"""

import requests
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import mysql.connector
import time
import json,tweepy
import omdb
from collections import MutableMapping
from django_cron import CronJobBase, Schedule
from movie.models import Movie
from tweet.models import Tweet
from textblob import TextBlob


class MyCronJob(CronJobBase):

    class listener(StreamListener):

        def on_data(self, data):
            tweet_data_json={"movie_info":{}}
            all_data = json.loads(data)

            print tweet
            try:
                tweet = all_data["text"]
            except:
                return True
            for i in movie_names:
                if(i in tweet):
                    flag=0
                    movie_name=i
                    break
                else:
                    movie_name=''
                    flag=1

            if(flag==1):
                return True

            favourites=all_data["favorite_count"]
            username = all_data["user"]["screen_name"]
            created_at=all_data['created_at']
            try:
                place=all_data['place']['country'].encode('utf8')
            except:
                place=None           
                
            hashtags=all_data["entities"]['hashtags']
            if(hashtags==[]):
                all_hashtags=''
                names=[]
            else:
    #            print "here",
                names=[hashtag['text'].encode('utf8') for hashtag in hashtags]
                all_hashtags=','.join(names)
                
                
            urls=all_data["entities"]['urls']
            if(urls==[]):
                all_urls=''
                url=[]
            else:
                url=[url['display_url'].encode('utf8') for url in urls]
                all_urls=','.join(url)
	    
	    m = Movie.objects.get(pk=1)
            blob = TextBlob(tweet)
	    polarity = blob.polarity
	    subjectivity = blob.subjectivity
	    Tweet(movie = m , text = tweet, polarity = polarity , subjectivity = subjectivity).save()

            tweet_data_json["movie_info"]["tweet"]=tweet.encode('utf8')
            tweet_data_json["movie_info"]["favourites"]=favourites
            tweet_data_json["movie_info"]["username"]=username.encode('utf8')
            tweet_data_json["movie_info"]["created_at"]=created_at.encode('utf8')
            tweet_data_json["movie_info"]["hashtags"]=names
            tweet_data_json["movie_info"]["urls"]=url
            tweet_data_json["movie_info"]["place"]=place
            tweet_data_json["movie_info"]["movie_name"]=movie_name
            json_string=json.dumps(tweet_data_json)
            print json_string
            x = Movie.objects.filter(name = movie_name)
            print x
            if x.count() > 0:
                movie = Movie.objects.get(name = movie_name)
                print movie.name
            else:
                print 'bad luck'
            return True

        def on_error(self, status):
            print status

    consumer_key = 'UYFW7uzEkVTbEjoA7MSG12ALj'
    consumer_secret = 'uObgLImI2FAv5hw2rkltwA8T8jcMNUaKEroFQxpSmg7vaQjHGL'
    access_token = '196910418-wgfpGYg3hSoXt3Q7j3lcBJqn7NztTiuRHc3S77uw'
    access_token_secret = 'iFEYYT0UeAYAkht1VoRM7vcwWo1P8KhOQBcGfzu51zSXt'


    while True:
        url_0='http://in.bookmyshow.com/national-capital-region-ncr#!quickbook'
        url='http://in.bookmyshow.com/serv/getData?cmd=QUICKBOOK&type=MT'
        s=requests.session()
        r=s.get(url_0)
        page=requests.get(url,cookies=r.cookies,verify=False)
        all_dict=json.loads(page.text)
        movie_names=[]
        for arr in all_dict['moviesData']['BookMyShow']['arrEvents']:
            if(arr['ChildEvents'][0]['EventLanguage']== 'Hindi' or arr['ChildEvents'][0]['EventLanguage']== 'English'):
                movie_names.append(arr['EventTitle'].encode('utf8').replace(" ",""))
                movie_names.append(arr['EventTitle'].encode('utf8').replace(" ","").lower())
                if("-" in arr['EventTitle'].encode('utf8').replace(" ","")):
                    movie_names.append(arr['EventTitle'].encode('utf8').replace(" ","").replace("-",""))
                    movie_names.append(arr['EventTitle'].encode('utf8').replace(" ","").replace("-","").lower())
                if("." in arr['EventTitle'].encode('utf8').replace(" ","")):
                    movie_names.append(arr['EventTitle'].encode('utf8').replace(" ","").replace(".",""))
                    movie_names.append(arr['EventTitle'].encode('utf8').replace(" ","").replace(".","").lower())
                if("," in arr['EventTitle'].encode('utf8').replace(" ","")):
                    movie_names.append(arr['EventTitle'].encode('utf8').replace(" ","").replace(",",""))
                    movie_names.append(arr['EventTitle'].encode('utf8').replace(" ","").replace(",","").lower())
            else:
                break


        # for movie_twitter in Movie.objects.all():
        #     movie_names.append(movie_twitter.name)


        # for movie_title in movie_names:
        #     x = Movie.objects.filter(name = movie_title)
        #     if x.count() == 0:
        #         Movie(name = movie_title).save()
        #         # print movie_title
        #         # print 'saved'
        #     else:
        #         print movie_title
        #         # print 'not saved'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        try:
            api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
            twitterStream = Stream(auth, listener())
            twitterStream.filter(track=movie_names,languages=["en"])
            twitterStream.disconnect()
        except:
            continue
    
    
    

