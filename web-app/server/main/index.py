# @Author: valentin
# @Date:   2016-05-16T23:05:40+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-17T00:31:48+02:00

from . import main
from .. import socketio
from flask import render_template

from bluebirdlib.data import get_tweets, update_tweet

@main.route('/')
def index():
	return "Hello World"


@main.route('/tweets')
def tweets():
	# Get untagged tweets
	tweets = get_tweets({"depressed": {"$exists": False}})
	tweets = map(lambda x: {"id": x["id"], "text": x["text"]}, tweets)

	return render_template("tweets.html", tweets=tweets)

@socketio.on('add-positive', namespace='/tweets')
def add_positive(tweet_id):
	print tweet_id
	query = {"depressed": True}
	update_tweet({"id": int(tweet_id)}, query)

@socketio.on('add-negative', namespace='/tweets')
def add_negative(tweet_id):
	query = {"depressed": False}
	update_tweet({"id": int(tweet_id)}, query)
