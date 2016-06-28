from bluebirdlib.data import get_tweets
from bluebirdlib.user import get_next_users_to_display
from datetime import timedelta
from flask import Flask
from flask import Response
from flask import current_app
from flask import jsonify
from flask import make_response
from flask import request
from flask.ext.cors import CORS
from functools import update_wrapper
import os
import time

MAX_USER = 4

app = Flask(__name__, static_url_path="")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/fetch_users/<int:nb_users>', methods=['GET'])
def fetch_users(nb_users):
	if nb_users < 0:
		return make_response("ERROR", 404)
	if nb_users > MAX_USER:
		nb_users = MAX_USER
	users = [x['user_id'] for x in get_next_users_to_display(nb_users)]
	resp = jsonify({'users': users})
	resp.status_code = 200
	return resp


@app.route('/fetch_tweets/<user_id>', methods=['GET'])
def fetch_user_tweets(user_id):
    tweets = [tweet['text'] for tweet in get_tweets(filters={'user.id': {'$eq': long(user_id)}})]
    resp = jsonify({'tweets': tweets})
    resp.status_code = 200
    return resp


@app.route('/tag_user', methods=['POST'])
def tag_user():
	params = request.json
	print params
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
