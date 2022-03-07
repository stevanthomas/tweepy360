from cgitb import text
from email.utils import parsedate
from ssl import create_default_context
from unicodedata import name
from unittest.mock import create_autospec
import tweepy
from tweepy import OAuthHandler
from tweepy import Cursor
import pandas as pd
########################Credentials###################################
##test
ACCESS_TOKEN = 
ACCESS_SECRET = 
CONSUMER_KEY = 
CONSUMER_SECRET = 


############ Connecting to the API


def connect_to_twitter():
	'''A function that connects to the Twitter API using tweepy's OAuthHandler. Returns an API object'''

	auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

	api = tweepy.API(auth)
	return api

########### Creating the API object

api = connect_to_twitter()


########### Test to check if it worked


test_tweets = api.home_timeline()
for tweet in test_tweets:
	print(tweet.text)   


############ Tweets from a specific handle (Eg: PFERD!!!!)

ford_tweets = api.user_timeline(screen_name  = 'Ford')
for tweet in ford_tweets:
	print(tweet.text)
#print(ford_tweets)


def get_tweets(twitter_user_name, page_limit = 16, count_tweets = 200):
	"""
	@params
		-twitter_user_name: The user name of the company/individual
		-page_limit: Total number of pages extracted. Default value = 16
		-count_tweet: Maximum number to be retrieved form a page. Default value = 200
	
	"""
	all_tweets = []
	
	for page in tweepy.Cursor(api.user_timeline,screen_name = twitter_user_name, count = count_tweets).pages(page_limit):
		for tweet in page:
			parsed_tweet = {}
			parsed_tweet['id'] = tweet.id_str
			parsed_tweet['date'] = tweet.created_at
			parsed_tweet['author'] = tweet.user.name
			parsed_tweet['twitter_name'] = tweet.user.screen_name
			parsed_tweet['text'] = tweet.text
			parsed_tweet['number of likes'] = tweet.favorite_count
			parsed_tweet['number_of_retweets'] = tweet.retweet_count

			all_tweets.append(parsed_tweet)

	#Converting to a dataframe
	df = pd.DataFrame(all_tweets)
	# Dropping duplicates in the data
	df = df.drop_duplicates( "text", keep = 'first')

	return df

data = get_tweets('Ford',150,5000)
print(len(data))
 
data.to_csv("tweets.csv")