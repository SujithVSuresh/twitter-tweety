import tweepy


bearer_token="...your_bearer_token"
client = tweepy.Client(bearer_token)

query = 'from:elonmusk -is:retweet'
tweets = client.search_recent_tweets(query=query, max_results=100)

length = len(tweets.data)

for index, tweet in enumerate(tweets.data, start=1):
    print(f"{index})",tweet)
       

    
