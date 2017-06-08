import tweepy, time
from credentials import *

#access the Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)       
        
#open the text file, read all the lines into a list, then remove and return the first line
with open('SongofKanye.txt') as f:
    lines = f.readlines()
    tweet = lines.pop(0)

#tweet out that first line
api.update_status(tweet)

#rewrite the text file to include everything but the tweeted line, essentially deleting a line from the text file every time it's tweeted 
output_file = open('SongofKanye.txt', 'w')

for write_line in lines:
    output_file.write(write_line)
