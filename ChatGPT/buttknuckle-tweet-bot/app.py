import tweepy
import time
import random

# Replace the placeholders with your own Twitter API keys
auth = tweepy.OAuthHandler('q5D8Ina6g7V4C6PcZXEVxVrYh', 'lAhS1M6nVQxvosZlgZ24Grfh9NFKUuz8s4s3GftIomkJUGPGWc')
auth.set_access_token('255856851-Q6z2xCAdYFKB5WTTAfF1Yg8uTksB8FVyvv8iQOSY', 'fHgOtg19nmqDMqy2JWYwFMFploGuA1gj2IK6or6YtBGj5')

bearer_token = 'AAAAAAAAAAAAAAAAAAAAADR8fQEAAAAAtlgz3z%2FyJn5tBwDFTfMi1WU%2FZrA%3DHjZh4JaN0zMlnqdy8YfTiEMyezDTjDqX3GVFyDl8bOzSpWo9Hg'

api = tweepy.API(auth)

response = api.home_timeline()

# Print the text of each tweet
for tweet in response:
    print(tweet.text)

# # This function will be called every minute to tweet a random message
# def tweet():
#     messages = [
#         'Hello, world!',
#         'This is a Twitter bot.',
#         'I can tweet messages automatically.',
#     ]

#     # Pick a random message from the array
#     message = messages[int(random.random() * len(messages))]

#     # Post the message to Twitter
#     api.update_status(message)
#     print(f"Tweeted: {message}")

# # # Tweet a message every minute
# # while True:
# #     tweet()
# #     time.sleep(60)

# tweet()