#  -*- coding: utf-8 -*-


#----------------------------------------------------------------------------------------------#

#                                       Created/Credited by                                    #

#                                        Kibeom Alex Hong                                      #

#----------------------------------------------------------------------------------------------#





from tweepy.streaming import StreamListener

from tweepy import OAuthHandler

from tweepy import Stream

import tweepy


consumer_key = 'UjnHPModDzohpESefLeSCncAk'
consumer_secret = '2OWQ9zYinzMZB3gUQx3o3tfIdt0JX2x00hRoBJqcxBN9I5E4nv'
access_token = '988327751126925312-ts0LnQL22Cb1IOPnrHyobyu6BVWjTsO'
access_token_secret = '9aRnHHOcLwVsHfw2264JebZQExWZKAZAxW2b6eOKGLF5D'


#Variables that contains the user credentials to access Twitter API




# Your tokens / keys



#-----------------------------------------------------------------------



# Save JSON file to the text file

tweets = open("live_tweets_recorded.txt","w")



#-----------------------------------------------------------------------



#This is a basic listener that just prints received tweets to stdout.

class StdOutListener(StreamListener):



    def on_data(self, data):

        print (data)

        tweets.write(data)

        return True



    def on_error(self, status):

        print (status)





if __name__ == '__main__':



    #This handles Twitter authetification and the connection to Twitter Streaming API

    l = StdOutListener()

    auth = OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)



    stream = Stream(auth, l)



    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['Australia'])

    #                     ^^^^^^^^^^^^^^

    #                      Hashtag

tweets.close()