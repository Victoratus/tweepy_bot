import tweepy
import random
import pickle
from dialogo import *
from keys import *
from user_data import *

def login(rate_limit = True):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	if (rate_limit == True): 
		api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
	else:
		api = tweepy.API(auth, compression=True)
	return api

def seguir_a_los_seguidores_de(api, nombre, numero_de_seguidores = -1):
	if numero_de_seguidores == -1:
		for follower in tweepy.Cursor(api.followers_ids, id = nombre).items():
			if (follower != api.me().id): 
				api.create_friendship(follower)

	else:
		for follower in tweepy.Cursor(api.followers_ids, id = nombre).items():
			if (follower != api.me().id): 
				api.create_friendship(follower)
				numero_de_seguidores = numero_de_seguidores - 1
				if numero_de_seguidores == -1:
					return

def twittear_frase_aleatoria(api):
	frase = frase_aleatoria()
	api.update_status(frase)
	print("He twitteado: \"" + frase + "\"")

def dar_like_a(api, numero_de_tweets, search):
	for tweet in tweepy.Cursor(api.search, search).items(numero_de_tweets):
	    try:
	    	if tweet.lang == "es":
		        tweet.favorite()
		        print("He dado like a: \"" + tweet.text + "\"")

	    except tweepy.TweepError as e:
	        print(e.reason)

	    except StopIteration:
	        break

def retwittear(api, numero_de_tweets, search):
	for tweet in tweepy.Cursor(api.search, search).items(numero_de_tweets):
	    try:
	    	if tweet.lang == "es":
		        tweet.retweet()
		        print("He retwitteado: \"" + tweet.text + "\"")

	    except tweepy.TweepError as e:
	        print(e.reason)

	    except StopIteration:
	        break

def imprimir_tweets(api, numero_de_tweets, search):
	for tweet in tweepy.Cursor(api.search, search, tweet_mode = "extended").items(numero_de_tweets):
	    try:
	        if tweet.lang == "es":
	        	print("\"" + tweet.full_text + "\"")	        

	    except tweepy.TweepError as e:
	        print(e.reason)

	    except StopIteration:
	        break

def guardar_tweets(api, archivo, numero_de_tweets, search, incluir_respuestas = True):
	tweets = []
	for tweet in tweepy.Cursor(api.search, search + " -filter:retweets", tweet_mode = "extended").items(numero_de_tweets):
	    try:
	        if tweet.lang == "es" and (incluir_respuestas or tweet.full_text[0] != '@'):
	        	tweets.append(tweet)

	    except tweepy.TweepError as e:
	        print(e.reason)

	    except StopIteration:
	        break
	pickle.dump(tweets, archivo)

def tweetear_tweets(api, tweets, preguntar = False):
	
	if preguntar == True:
		for tweet in tweets:
			control = input("Tweeteo \"" + tweet.full_text + "\"? ")
			if control == 's':
				api.update_status(tweet.full_text)
				print("Twitteado: \"" + tweet.full_text + "\"")

	else:
		for tweet in tweets:
			api.update_status(tweet.full_text)
			print("Twitteado: \"" + tweet.full_text + "\"")

def dejar_de_seguir(api, name, all = True, num = 0):
	num_dejados = 0
	if all == True:
		for friend in api.friends_ids(name):
			api.destroy_friendship(friend)
			num_dejados = num_dejados+1

	else:
		for friend in api.friends_ids(name):
			api.destroy_friendship(friend)
			num = num-1
			if num < 0:
				break
			num_dejados = num_dejados+1

	print("He dejado de seguir a " + str(num_dejados) + " seguidos")

def refrescar_seguidores_lista(api, range_min = 50, range_max = 200):
	dejar_de_seguir(api)
	seguir_a_los_seguidores_de(api, nombres_madridistas[random.randint(0,num_madridistas-1)], random.randint(range_min, range_max))
	print("Seguidores refrescados")

def refrescar_seguidores_busqueda(api, range_min = 50, range_max = 200, busqueda = "madridista"):
	dejar_de_seguir(api)
	seguir_busqueda(api, range_min, range_max, busqueda)

	print("Seguidores refrescados")

def seguir_busqueda(api, range_min = 50, range_max = 200, busqueda = "madridista"):
	num = random.randint(range_min, range_max)
	num_it = num/20
	n = 0
	while num_it > 0:
		if num_it != 0: users = api.search_users(busqueda, 20, 1)
		else: users = api.search_users(busqueda, num%20, 1)
		for user in users:
			api.create_friendship(user.id)
			n = n + 1
		num_it = num_it - 1

	print("Seguido a " + str(n) + " usuarios")

def prueba2(api, busqueda, range_min = 50, range_max = 200):
	num = random.randint(range_min, range_max)
	num_it = num/20
	n = 0
	while num_it > 0:
		if num_it != 0: users = api.search_users(busqueda, 20, 1)
		else: users = api.search_users(busqueda, num%20, 1)
		for user in users:
			n = n + 1
		num_it = num_it - 1

	print(n)