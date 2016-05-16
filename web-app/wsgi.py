# @Author: valentin
# @Date:   2016-05-16T22:50:49+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-16T23:03:18+02:00

from gevent import monkey
monkey.patch_all()
from server import create_app, socketio

app = create_app(True)

if __name__ == '__main__':
    socketio.run(app)
