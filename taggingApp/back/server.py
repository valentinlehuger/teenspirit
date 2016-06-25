from bluebirdlib.data import get_tweets
from bluebirdlib.user import get_next_users_to_display
from flask import Flask
from flask import Response
from flask import jsonify
from flask import request
import os
import time


app = Flask(__name__, static_url_path="")

server_path = "new-webapp"
save_file = "tweets.json"
save_file_path = os.path.join(server_path, save_file)


@app.route('/fetch_users', methods=['GET'])
def fetch_users():
    users = [x["user_id"] for x in get_next_users_to_display(10)]
    resp = jsonify({'users': users})
    resp.status_code = 200
    return resp


@app.route('/fetch_tweets/<user_id>', methods=['GET'])
def fetch_user_tweets(user_id):
    tweets = [tweet['text'] for tweet in get_tweets(filters={"user.id": {"$eq": long(user_id)}})]
    resp = jsonify({"tweets": tweets})
    resp.status_code = 200
    return resp


@app.route('/tag_user', methods=['POST'])
def tag_user():
    params = request.json
    user_id = params.get("user_id", None)
    tag_name = params.get("tag_name", None)
    tag_value = bool(params.get("tag_value", False))

    query = {
        "date": time.strftime('%Y-%m-%d %H:%M:%S'),
        tag_name: tag_value
    }
    # add_control_to_user(long(user_id), query)
    resp = jsonify({})
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3033)), debug=True)
