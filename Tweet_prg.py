# importing the module
import tweepy
 
# personal details
consumer_key ="nkxfKBNPK8TELZjVKoJ7ETjeZ"
consumer_secret ="PShVPwZzZ9Sj4TjHoMiAkW4i651Bjv7l1YMwLcs3rRpap0yt4p"
access_token ="967251940324364288-seycUaIrkVjC4HoVLDFh54nlKSYZEw2"
access_token_secret ="ayXvlWS5M36L0IxWAFXU8K02au3pinI3G42xSYv5nCCws"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Manisha here !")
