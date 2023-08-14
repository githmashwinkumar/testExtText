import datetime
import locale

import tweepy as tw
import pandas as pd


api_key = 'EvTZjB6CCYHsN6YrKMwqsBmtI'
api_key_secret = 'RP0L4p6SPtXPdNUJRwNhrD1WlCFeMwnmV3sGHiuAB7ZbJTxzS1'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAE3aewEAAAAAZywXT%2Fw1yKufHGaOeQA1TAuRf7U%3DAsu1hLiOjJs6cXvKgGPksjTxTOxZBOQqWelOfjXVgE1oKsMUeu'
access_token = '80850353-wZtFmlBpEdnhPU4lqNgMzpQCsVT6tkfkWXcmphDIR'
access_token_secret = '26HiFKSUHjQskPSMm278E9raFWwqJDoJVcHGPUCJUEQmC'

auth = tw.OAuthHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
search_query = "Narendra Modi"
no_of_tweets = 200

try:
    tweets = api.search_tweets(q=search_query, lang='en', count=no_of_tweets, tweet_mode='extended')
    for tweet in tweets:
        print(tweet)
except BaseException as e:
    print(e)

#auth = tw.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tw.API(auth, wait_on_rate_limit=True)

#----------------------------------------------

