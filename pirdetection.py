import RPi.GPIO as GPIO
import time
import os
import tweepy
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

try:    
    print("PIR module test (CTRL+C to exit)")
    time.sleep(2)
    print("Motion Detected")
    consumer_key ="nkxfKBNPK8TELZjVKoJ7ETjeZ"
    consumer_secret ="PShVPwZzZ9Sj4TjHoMiAkW4i651Bjv7l1YMwLcs3rRpap0yt4p"
    access_token ="967251940324364288-seycUaIrkVjC4HoVLDFh54nlKSYZEw2"
    access_token_secret ="ayXvlWS5M36L0IxWAFXU8K02au3pinI3G42xSYv5nCCws"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    b=1
    a=0
    while a<=2 :
        img="/home/pi/Desktop/img.jpg"
        cmd="fswebcam -F 3 --fps 20 -r 800x600 "+img
        os.system(cmd)
        print("Pic taken!")
        api.update_with_media(img, status="Nice one")
        print("wait for 5 seconds!")
        time.sleep(1)
        a+=1
        b+=1
        print("Done")
        

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()

