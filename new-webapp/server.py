import os
import json
from flask import Flask, Response, request

app = Flask(__name__, static_url_path="")
app.add_url_rule("/", "root", lambda: app.send_static_file("index.html"))


@app.route('/api/tweets', methods=['GET', 'POST'])
def comments_handler():
        with open('tweets.json', 'r') as f:
            comments = json.loads(f.read())

        if request.method == 'POST':
            new_comment = request.form.to_dict()
            new_comment['id'] = int(time.time() * 1000)
            comments.append(new_comment)

            with open('tweets.json', 'w') as f:
                f.write(json.dumps(comments, indent=4, separators=(',', ': ')))

        return Response(
            json.dumps(comments),
            mimetype='application/json',
            headers={
                'Cache-Control': 'no-cache',
                'Access-Control-Allow-Origin': '*'
            }
        )

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3000)), debug=True)
