from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import twitter_keys
import tweepy
import csv
import pandas as pd

#
#try:
#    os.remove("tweets.json")
#except:
#    pass
#
## Criando a lista de palavras-chave que serão rastreadas
#tracklist = ['Manchester United', 'Champions League']
#
#with open('tracklist.json', 'w') as tl:
#    tl.write(str(tracklist))
#
## Iniciando as variáveis globais
#tweet_count = 0
#
## Entre com o número de tweets que serão baixados
#n_tweets = 1

# Classe que irá possibilitar o streaming de tweets
class luisa(StreamListener):
      
    def __init__(self,tweet_count,n_tweets,tracklist):
        self.tweet_count = tweet_count
        self.n_tweets = n_tweets
        self.tracklist = tracklist
        
    def limpa_arq(self):
        try:
            os.remove("tweets.json")
        except:
            pass
        
        # Criando a lista de palavras-chave que serão rastreadas
#        tracklist = ['Manchester United', 'Champions League']
        
        with open('tracklist.json', 'w') as tl:
            tl.write(str(self.tracklist))

        
    def roda(self):
        
        
#        global tweet_count
#        global n_tweets
#        tweet_count = 0
#        global stream
#        
        if self.tweet_count < self.n_tweets:
#            
#            print(data)
#            with open('tweets.json', 'a') as f:
#                f.write(data)
#            self.tweet_count += 1
#            
#            return True
#        else:
#            return False
##            stream.disconnect()
            auth = tweepy.OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
            auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            
            # Criando um arquivo para inserir os tweets
            csvFile = open('tweets.json', 'a')
            
            # Usando um csv Writer
            csvWriter = csv.writer(csvFile)
            
    #        subject_list = ['Trump', 'Obama']
    #        n_tweets = 10
            
            with open('tracklist.json', 'w',encoding="utf-8") as tl:
                tl.write(str(self.tracklist))
            
            for tweet in tweepy.Cursor(api.search, q=self.tracklist, count=2,
                                       lang='en', since='2019-06-11').items(self.n_tweets):
                print (tweet.created_at, tweet.text)
                csvWriter.writerow([tweet.created_at, tweet.text])
                return True
        else:
            return False
    def on_error(self, status):
        print(status)


#
#
#tweet_count = 0
#n_tweets = 10
#lista = ['obama']
#
#l = luisa(tweet_count,n_tweets,lista)
#l.limpa_arq()
##auth = OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
##auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
#stream = Stream(auth, l)
#stream.filter(track=lista, languages=["en"])