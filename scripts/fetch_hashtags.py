# @Author: valentin
# @Date:   2016-05-16T21:24:01+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-16T21:55:26+02:00

from bluebirdlib.connection import get_api
from bluebirdlib.status import getTweetFromHashTag
from bluebirdlib.data import add_to_mongo, is_exists

from sys import argv
import pprint
import json


def main(search, api):
        tweets = map(lambda x: x.AsDict(), getTweetFromHashTag(search, api))
        map(lambda x: add_to_mongo(x) if not is_exists(x["id"]) else None, tweets)
        return 0

if __name__ == "__main__":
        if argv < 2:
                print "usage ./fetch_hastag.py research"
        else:
                search = argv[1]
                api = get_api(argv[2])
                main(search, api)
