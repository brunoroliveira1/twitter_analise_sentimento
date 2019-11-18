

import streaming_api as streaming
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import twitter_keys
import request
import json
import pandas as pd
import numpy as np
import analyzer_tweets as anal
import historic_api as historico
import matplotlib.pyplot as plt

import preprocessor as p
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import re
import json
import string
from collections import Counter

from Repositorio_codes.front.site.nuvem_palavras import nuvem

global stream

from flask import (Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response,jsonify,send_file)

app = Flask(__name__)
app.secret_key = 'icc'


class Busca:
    def __init__(self, busca):
        self.busca = busca


lista = []


@app.route('/')
def novo():
    return render_template('novo.html', titulo='ICC - Trabalho Busca Twitter')


@app.route('/criar', methods=['POST', ])
def criar():
    lista = request.form['busca']

    tweet_count = 0
    n_tweets = int(request.form['qtd'])
    #tipo = (request.form['tipo'])


    tipo = "Historico"

    if tipo == "Stream":
    
        l = streaming.Tempo_real(tweet_count,n_tweets,lista)
        l.limpa_arq()
        auth = OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
        auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, l)
        stream.filter(track=lista, languages=["en"])
        stream.disconnect()
        
        a = anal.analisar(tipo)
        a.rodar()
#        
        return render_template('imagem.html')
        
    else:
        h=historico.historico(lista,n_tweets)
        h.roda()
        n=nuvem('historico')
        n.geranuvem()
#        return send_file('foo.png', mimetype='image/gif')
        return render_template('dadosGerais.html', titulo='Busca no Twitter', procuras=lista)
       
       
    
#    # Recupera o arquivo JSON com os tweets rastreados
#    tweets_data_path = 'tweets.json'
#    tweets_data = []
#
#    tweets_file = open(tweets_data_path, 'r')
#    for line in tweets_file:
#        try:
#            tweet = json.loads(line)
#            tweets_data.append(tweet)
#        except:
#            continue
#
#    # Cria um DataFrame com alguns campos importantes do JSON
#    tweets = pd.DataFrame()
#    tweets['Username'] = list(map(lambda tweet: tweet['user']['screen_name'], tweets_data))
#    tweets['Text'] = list(map(lambda tweet: tweet['text'], tweets_data))
#    tweets['Location'] = list(map(lambda tweet: tweet['user']['location'], tweets_data))
#    tweets['Timestamp'] = list(map(lambda tweet: tweet['created_at'], tweets_data))
    
    
#    return render_template('simple.html',  tables=[tweets.to_html(classes='data')], titles=tweets.columns.values)


@app.route('/pesquisa')
def pesquisa():
    return render_template('lista.html', titulo='Busca no Twitter', procuras=lista)

@app.route('/Estatistica')
def estatistica():
    return render_template('Estatistica.html', titulo='Estatisticas')


@app.route('/dadosGerais')
def dadosgerais():
    return render_template('dadosGerais.html', titulo='Dados Gerais')


app.run(debug=True)
