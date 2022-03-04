import tweepy
########################Credentials###################################
##test
ACCESS_TOKEN = '<INSERT YOUR TOKEN HERE>'
ACCESS_SECRET = '<INSERT YOUR ACCESS SECRET HERE>'
CONSUMER_KEY = '<INSERT CONSUMER KEY HERE'
CONSUMER_SECRET = '<INSERT YOUR SECRET HERE. MINE IS THAT I LIKE HELLO KITTY'>


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


############ Tweets from a specific handle (Eg: PFERD!!!)

ford_tweets = api.user_timeline('realdonaldtrump')
for tweet in ford_tweets:
	print(tweet.text)
	print(tweet)


