# @Author: valentin
# @Date:   2016-05-16T23:05:40+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-17T00:31:48+02:00

from . import main
from .. import socketio
from flask import render_template
import time

from bluebirdlib.data import get_tweets
from bluebirdlib.user import get_next_users_to_display

TWEET = USER = []
    
def fetch_new_user():

    global TWEET
    global USER

    USER.pop(0)
    TWEET.pop(0)
    user = get_next_users_to_display(1)
    USER.append(user)
    tweet = get_tweets(filters={"user.id": {"$in": map(lambda user: user["user_id"], user)}})
    TWEET.append(tweet)
    print "HERE\n"
    print tweet

@main.route('/')
def index():
        return "Hello World"

@main.route('/tweets')
def tweets():
    global TWEET
    global USER
    # Get untagged tweets
    print "Get Users"
    users = get_next_users_to_display(2)
    # users = map(lambda x: {"id": x["user_id"]}, users)
    tweets = get_tweets(filters={"user.id": {"$in": map(lambda user: user["user_id"], users)}})
    TWEET.append(tweets)
    USER.append(users)
    return render_template("tweets.html", tweets=TWEET[0], user=USER[0])

@socketio.on('add-positive', namespace='/tweets')
def add_positive(user_id):
    fetch_new_user()
    query = {"date": time.strftime('%Y-%m-%d %H:%M:%S'), "depressed": True}
    add_control_to_user({"id": int(user_id)}, query)

@socketio.on('add-negative', namespace='/tweets')
def add_negative(user_id):
    fetch_new_user()
    query = {"date": time.strftime('%Y-%m-%d %H:%M:%S'), "depressed": False}
    add_control_to_user({"id": int(user_id)}, query)

