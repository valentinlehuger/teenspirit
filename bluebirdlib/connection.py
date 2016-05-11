# @Author: valentin
# @Date:   2016-05-11T22:25:28+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-11T22:41:13+02:00

import twitter
import os

def get_api(project_path):
	with open(os.path.join(project_path, '.tokens.txt'), 'r') as tokensfile:
		try:
			keys = [[x.strip() for x in line.split(':')][1] for line in tokensfile.readlines()]
		except:
			raise("Impossible to load api keys")
	try:
		api = twitter.Api(consumer_key=keys[0],
		                  consumer_secret=keys[1],
		                  access_token_key=keys[2],
		                  access_token_secret=keys[3])

		return api
	except:
		raise("Impossible to get Twitter api")
