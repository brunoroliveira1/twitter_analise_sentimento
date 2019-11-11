# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:02:55 2019

@author: luisa
"""

import streaming_api as streaming
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import twitter_keys

import twitter_keys

tweet_count = 0
n_tweets = 1
tracklist = ['Manchester United', 'Champions League']

l = streaming.luisa(tweet_count,n_tweets,tracklist)
l.limpa_arq()
auth = OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
stream = Stream(auth, l)
stream.filter(track=tracklist, languages=["en"])
