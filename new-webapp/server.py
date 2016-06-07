import os
import json
from flask import Flask, Response, request

app = Flask(__name__, static_url_path="")
app.add_url_rule("/", "root", lambda: app.send_static_file("index.html"))

server_path = "new-webapp"
save_file = "tweets.json"
save_file_path = os.path.join(server_path, save_file)

@app.route('/api/tweets', methods=['GET', 'POST'])
def comments_handler():

    if save_file not in os.listdir(server_path):
        with open(save_file_path, "w+") as f:
            json.dumps({})

    with open(save_file_path, "r") as f:
        tweets = json.loads(f.read())

    if not tweets:
        # fetch_users
        print "Have to fetch users"
    for user in tweets:
        if tweets[user]:
            user_tweets = tweets[user]
            del tweets[users]
            with open(save_file_path, "w") as f:
                f.write(json.dumps(tweets, indent=4, separators=(',', ': ')))
            return user_tweets

    for idx, user in enumerate(tweets):
        if idx < 2:
            tweets[user] = fetch_tweets(user)
        else:
            break

    # return Response(
    #     json.dumps(tweets),
    #     mimetype='application/json',
    #     headers={
    #         'Cache-Control': 'no-cache',
    #         'Access-Control-Allow-Origin': '*'
    #     }
    # )

@app.route('/api/answer', methods=['POST']):
    return



if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3000)), debug=True)
