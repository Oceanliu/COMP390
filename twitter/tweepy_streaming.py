import sys
import tweepy
from tweepy.utils import import_simplejson
from pymongo import Connection

consumer_key="wCQxoTro2ADP7wbfztPaw"
consumer_secret = "0ovXdI1CcGVz0ZMb8jNThqAD2rLFA0D2ga3BZKLLgKI"
access_key="1168170264-dZwtgfhF39j3WlXniiPvHFkHlHbmNm1hIl7Hy60"
access_secret = "X7whh4xVymr2go0T7zi8Z9T8byCaB9ceAr25FJrijY" 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
print 'reach here'
connection = Connection('localhost', 27017)
db = connection.strem_testm
posts = db.stream_collection

class CustomStreamListener(tweepy.StreamListener):
	
    posts
    json = import_simplejson()

    def __init__(self,posts = None, api = None, fprefix = 'streamer'):
	self.api = api
	self.posts = posts
	self.fprefix = fprefix

    def on_status(self, status):
	print '**********************************'
	print status.author.screen_name.encode("utf-8")
	print status.author.name.encode("utf-8")
	print status.text.encode("utf-8")
	post = {
		"author_screen_name":status.author.screen_name.encode("utf-8"),
		"author_followers":status.author.followers_count,
		"author_verified":status.author.verified,
		"author_location":status.author.location,
		"author_status_count":status.author.statuses_count,
		"author_friend_count":status.author.friends_count,
		"author_lang":status.author.lang,
		"text":status.text.encode("utf-8"),
		"retweet_count":status.retweet_count,
		"source":status.source,
		"create_time":status.created_at}
	self.posts.insert(post)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(posts,api))
sapi.filter(track=['diaoyu','China','senkaku', 'Japan'])

