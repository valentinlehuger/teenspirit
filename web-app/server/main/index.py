# @Author: valentin
# @Date:   2016-05-16T23:05:40+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-17T00:31:48+02:00

from . import main
from server import socketio
from flask import render_template
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
    return "Hello World"

@main.route('/tweets')
def tweets():
    global TWEET
    global USER
    # Get untagged tweets
    print "Get Users"
    [USER.append(user['user_id']) for user in get_next_users_to_display(2)]
    for user in USER:
        user_tweets = []
        tweets = get_tweets(filters={"user.id": {"$eq": user}})
        [user_tweets.append(tweet['text']) for tweet in tweets]
        if len(user_tweets) > 1:
            TWEET.append(user_tweets)
    return render_template("tweets.html", tweets=TWEET[0], user=USER[0])

@socketio.on('add-positive', namespace='/tweets')
def add_positive(user_id):
    print "in positive"
    query = {"date": time.strftime('%Y-%m-%d %H:%M:%S'), "depressed": True}
    add_control_to_user(long(user_id), query)
    fetch_new_user()
    return render_template("tweets.html", tweets=TWEET[0], user=USER[0])

@socketio.on('add-negative', namespace='/tweets')
def add_negative(user_id):
    query = {"date": time.strftime('%Y-%m-%d %H:%M:%S'), "depressed": False}
    add_control_to_user(long(user_id), query)
    fetch_new_user()
    return render_template("tweets.html", tweets=TWEET[0], user=USER[0])
