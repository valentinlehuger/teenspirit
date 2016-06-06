# @Author: valentin
# @Date:   2016-05-16T23:05:40+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-06-07T00:14:59+02:00

from . import main
from .. import socketio
from flask import render_template, redirect
import time

from bluebirdlib.data import get_tweets
from bluebirdlib.user import get_next_users_to_display, add_control_to_user

TWEET = []
USER = []

def fetch_new_user():

    global TWEET
    global USER

    USER.pop(0)
    TWEET.pop(0)
    new_user = [user['user_id'] for user in get_next_users_to_display(2)]
    USER.append(new_user[1])
    ## TODO: Sortir ce passage dans une fonction car similaire a la methode tweets
    # attention si user_tweets est vide il faudra rappeler la methode.
    user_tweets = []
    tweets = get_tweets(filters={"user.id": {"$eq": new_user[1]}})
    [user_tweets.append(tweet['text']) for tweet in tweets]
    if len(user_tweets) > 1:
        TWEET.append(user_tweets)

@main.route('/')
def index():
    return "<a href=/tweets>Tweets</a>"


def fetch_users():
	global USER
	[USER.append(user['user_id']) for user in get_next_users_to_display(50)]

def fetch_tweets():
	global TWEET
	for i in range(0, min(len(USER), 2) - len(TWEET)):
		user_tweets = [tweet["text"]
					  for tweet
					  in get_tweets(filters={"user.id": {"$eq": USER[len(TWEET) + i]}})]
        if len(user_tweets) > 1:
            TWEET.append(user_tweets)


@main.route('/tweets')
def tweets():
	if not USER:
		fetch_users()
	fetch_tweets()

	return render_template("tweets.html", tweets=TWEET[0], user=USER[0])

@socketio.on('add-positive', namespace='/tweets')
def add_positive(user_id):
    print "in positive"
    query = {"date": time.strftime('%Y-%m-%d %H:%M:%S'), "depressed": True}
    add_control_to_user(long(user_id), query)
    return redirect("/tweets")

@socketio.on('add-negative', namespace='/tweets')
def add_negative(user_id):
    query = {"date": time.strftime('%Y-%m-%d %H:%M:%S'), "depressed": False}
    add_control_to_user(long(user_id), query)
    return redirect("/tweets")
