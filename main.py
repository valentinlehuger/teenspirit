# @Author: valentin
# @Date:   2016-05-11T22:39:27+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-11T23:14:36+02:00

from bluebirdlib.connection import get_api
from bluebirdlib.status import getTweetFromHashTag

from sys import argv
import pprint
import json

if __name__ == "__main__":
	if argv < 2:
		print "usage ./main.py research <json_output_file>"
	else:
		search = argv[1]
		api = get_api("./")
		tweets = map(lambda x: x.AsDict(), getTweetFromHashTag(search, api))

		if len(argv) > 2:
			try:
				with open(argv[2]+".json", 'w') as outputfile:
					json.dump(tweets, outputfile)
					print("dump result into {}".format(argv[2]))
			except:
				raise Exception("Impossible to create outputfile")
		else:
			pp = pprint.PrettyPrinter(indent=2)
			pp.pprint(tweets)
