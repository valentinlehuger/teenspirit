# @Author: valentin
# @Date:   2016-05-16T23:04:45+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-16T23:39:35+02:00

from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.socketio import SocketIO

socketio = SocketIO()

def create_app(debug=False):
	"""Create an application."""
	app = Flask(__name__)
	Bootstrap(app)
	app.debug = debug
	app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	socketio.init_app(app)
	return app
