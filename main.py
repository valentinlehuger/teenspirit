# @Author: valentin
# @Date:   2016-05-11T22:39:27+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-11T22:52:25+02:00

from bluebirdlib.connection import get_api
from bluebirdlib.status import getTweetFromHashTag

from sys import argv

if __name__ == "__main__":
	if argv < 2:
		print "usage ./main.py <research>"
	else:
		search = argv[1]
		api = get_api("./")
		tweets = map(lambda x: x.AsDict(), getTweetFromHashTag(search, api))
		print tweets[0]
