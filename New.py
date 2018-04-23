#  -*- coding: utf-8 -*-
import tweepy


consumer_key = 'UjnHPModDzohpESefLeSCncAk'
consumer_secret = '2OWQ9zYinzMZB3gUQx3o3tfIdt0JX2x00hRoBJqcxBN9I5E4nv'
access_token = '988327751126925312-ts0LnQL22Cb1IOPnrHyobyu6BVWjTsO'
access_token_secret = '9aRnHHOcLwVsHfw2264JebZQExWZKAZAxW2b6eOKGLF5D'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
num = 0
print (num)
for tweet in public_tweets:
    num = num + 1
    print (num)
    print (tweet.text)