

import streaming_api as streaming
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import twitter_keys
import request


global stream

from flask import (Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response)

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
    
    l = streaming.luisa(tweet_count,n_tweets,lista)
    l.limpa_arq()
    auth = OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
    auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)
    stream.filter(track=lista, languages=["en"])
    stream.disconnect()
    return redirect('/pesquisa')


@app.route('/pesquisa')
def pesquisa():
    return render_template('lista.html', titulo='Busca no Twitter', procuras=lista)

@app.route('/Estatistica')
def estatistica():
    return render_template('Estatistica.html', titulo='Estatisticas')


app.run(debug=True)
