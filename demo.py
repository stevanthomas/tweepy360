import tweepy
########################Credentials###################################

ACCESS_TOKEN = '1499463218229559297-Bq7TSxcCK0GKpvzC3uXyiYUJKVo3mE'
ACCESS_SECRET = 'wNssxfxywc22GWJCxoHErVZWz2zR93zEj67pQ50Q0hPwz'
CONSUMER_KEY = 'V7MYkA5PRGbvGrtmSe2UNOLZA'
CONSUMER_SECRET = 'YQtC0C0kxxCWrQApVpQtUb2CM1fy9HDwjBpU86q0BM9N6b0kFs'


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


