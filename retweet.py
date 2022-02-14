# Retweet bot for Twitter, using Python and Tweepy.
# Search query via hashtag or keyword.
# Author: Tyler L. Jones || CyberVox
# Date: Saturday, May 20th - 2017.
# License: MIT License.

import tweepy
from time import sleep
# Import in your Twitter application keys, tokens, and secrets.
# Make sure your keys.py file lives in the same directory as this .py file.
from keys import *
from keep_alive import keep_alive
import time
from replit import db

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

keep_alive()
interval = time.time()

# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# Where items(5), change 5 to the amount of retweets you want to tweet.
# Make sure you read Twitter's rules on automation - don't spam!

def retweet():
    for tweet in api.search_tweets(q='#alterpinay', count='1', result_type='mixed'):
        try:
            print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')   
            # if tweet.id_str in db.keys():
            tweet.retweet()
            print('Retweet published successfully.')
            db[tweet.id_str] = tweet.text     
            # else:
            #    retweet()

            # Where sleep(10), sleep is measured in seconds.
            # Change 10 to amount of seconds you want to have in-between retweets.
            # Read Twitter's rules on automation. Don't spam!
            # sleep(10)

        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except tweepy.errors.Unauthorized as error:
            print('\nError. Retweet not successful. Reason: ')
            print(error)

        except StopIteration:
            break

while True:
    print('Ticking')
    retweet()
    print('Ticked')
    time.sleep(300.0 - ((time.time() - interval) % 300.0))
