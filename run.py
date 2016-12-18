from __future__ import absolute_import, print_function
import forecastio
import json
import tweepy
#import key
import requests
import os
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
def func2():
        ckey='5S6e3TQH89WniAr1rnHKkZPNp'
        csecret='WD9GN0uzOqjsMfYwLfum1d921dagIpXmGmc62VqvHfHQVs63NC'
        atoken='2972097164-93xYPs0F3ilWa6f9ogAywqX0kcO9dCyNF6A3ZU4'
        asecret='WGQw1sE74oarrfRs5HUo2IAdb8FUlUzAawgxE9JnoLcye'
        auth=OAuthHandler(ckey,csecret)
        auth.set_access_token(atoken,asecret)
        api=tweepy.API(auth)
        with open(os.path.join('C:\\Users\\parul\\Desktop\\data.json')) as jfile:
                res=(json.load(jfile))
                print(res)
        """res = requests.get("https://quarkbackend.com/getfile/2013ecs35/pro15")
        res = json.loads(res.text)
        upcoming = res["upcoming"]"""
        upcoming=res["upcoming"]
        tweet = "Next contest: " + upcoming[0]["StartTime"] + "on " + upcoming[0]["Platform"] +". "+ upcoming[0]["url"]+" till " +upcoming[0]["EndTime"]
        api.update_status(status='[TweetPyMail]' + tweet)
        
def main():
        from parseweb import wr
        wr()
        func2()
        from mail import func1
        func1()
      
     
if __name__ == "__main__": main()
