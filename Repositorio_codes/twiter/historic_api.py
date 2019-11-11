import tweepy
import csv
import pandas as pd

import twitter_keys
import os

subject_list = ['Trump', 'Obama']
n_tweets = 10

class historico(object):
    
    
    def __init__(self, subject_list,n_tweets):
        self.subject_list = subject_list
        self.n_tweets = n_tweets

    
    def rodar(self):
        try:
            os.remove("historic.json")
        except:
            pass
        
        
        auth = tweepy.OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
        auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        
        # Criando um arquivo para inserir os tweets
        csvFile = open('historic.csv', 'a')
        
        # Usando um csv Writer
        csvWriter = csv.writer(csvFile)
        
#        subject_list = ['Trump', 'Obama']
#        n_tweets = 10
        
        with open('subject_list.json', 'w') as tl:
            tl.write(str(self.subject_list))
        
        for tweet in tweepy.Cursor(api.search, q=self.subject_list, count=2,
                                   lang='en', since='2019-06-11').items(self.n_tweets):
            print (tweet.created_at, tweet.text)
            csvWriter.writerow([tweet.created_at, tweet.text])





historico(subject_list,n_tweets)

