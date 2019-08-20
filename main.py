import tweepy

auth = tweepy.OAuthHandler("RoGKFsZzUhXVy1YB8fV7SuhZd", "xfNT7BCRyQtq6ODbOob0abiJWKcOKA6aAkrNbOy2cDsK69IjpO")
auth.set_access_token("627551780-OGd0URuYejI1NjAWWZ75LBvHVQ19rLd5w5QGStS6", "xURYDdrcSWzBy9kukOAjZNpNN2ldg5jDgKKtSaCTPpA7P")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)