import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)       
        

with open('SongofKanye.txt') as f:
    lines = f.readlines()
    tweet = lines.pop(0)
    
api.update_status(tweet)
    
output_file = open('SongofKanye.txt', 'w')

for write_line in lines:
    output_file.write(write_line)
