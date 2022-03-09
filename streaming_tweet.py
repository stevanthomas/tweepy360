from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy import Stream
from datetime import datetime
from kafka import KafkaProducer, KafkaClient
import json
import re
import sys



TWEET_TOPIC = 'Ford' #Setting the twitter handle of the account we wish to stream

##############################Credentials#############################
with open('credential.txt') as cred:
	lines = cred.readlines()

API_KEY = lines[0]
API_SECRET = lines[1]
ACCESS_TOKEN = lines[2]
ACCESS_SECRET = lines[3]


########## Creating the stream listener

KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'twitter_events'

class Streamer(Stream):
	
	def on_error(self,status_code):
		if staus_code == 402:
			return False

	def on_status(self,status):
		'''Basically an override on tweepy to add logic to the on_status part. On status is when everything is all clear to send across'''		
		if (not status.text.startswith('RT @')):
			producer.send(KAFKA_TOPIC, value = status._json)
			date = datetime.now()
			print(f'[{date.hour}:{date.minute}:{date.second}] sending tweet')

try:
	producer = KafkaProducer(bootstrap_servers =KAFKA_BROKER, value_serializer = lambda x: json.dumps(x).encode('utf-8'))
except Exception as e:
	print(f'Error Connecting to Kafka --> {e}')
	sys.exit(1)

############################Connecting to the API


def connecting_to_twitter():
	''' A function that connects to the twitter API and launches a stream of tweets'''
	streamer = Stream()
	auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

	api = tweepy.API(auth)
	stream = Stream(auth, streamer)
	stream.filter(track = TWEET_TOPIC, languages = ['en'])




