# @Author: valentin
# @Date:   2016-05-16T23:05:40+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-16T23:36:14+02:00

from . import main
from .. import socketio
from flask import render_template

from bluebirdlib.data import get_tweets

@main.route('/')
def index():
	return "Hello World"


@main.route('/tweets')
def tweets():
	# Get untagged tweets
	tweets = get_tweets({"depressed": {"$exists": False}})
	tweets = map(lambda x: {"id": x["id"], "text": x["text"]}, tweets)

	return render_template("tweets.html", tweets=tweets)
