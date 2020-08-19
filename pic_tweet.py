# importing the module
import os
import time
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
b=1
a=0
while a<=2 :
    img="/home/cs2017a122/Desktop/img.jpg"
    cmd="fswebcam -F 3 --fps 20 -r 800x600 "+img
    os.system(cmd)
    print("Pic taken!")
    api.update_with_media(img, status="Nice one")
    print("wait for 5 seconds!")
    time.sleep(5)
    a+=1
    b+=1
    print("Done")

