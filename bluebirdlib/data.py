# @Author: valentin
# @Date:   2016-05-14T01:46:03+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-16T23:26:20+02:00

from pymongo import MongoClient
import os
import json

def get_db(database, ip="ds011462.mlab.com", port=11462):
	return MongoClient("mongodb://valentin:valentin42" + '@%s:%d/' % (ip, port) + database)[database] or None


def add_json_object(object, filename):
    if os.path.exists(filename):
        f = open(filename, 'r')
        data = json.load(f)
        f.close()
    else:
        data = dict()
    f = open(filename, 'w')
    data.update(object)
    json.dump(data, f)
    f.close()
    return True


def add_to_mongo(object, connection=None):
	if connection is None:
	    db = get_db("teenspirit")
	else:
	    db = connection
	collection = db["tweets"]
	post_id = collection.insert(object, check_keys=False)
	return post_id


def is_exists(twitter_id, connection=None):
	if connection is None:
	    db = get_db("teenspirit")
	else:
	    db = connection
	collection = db["tweets"]
	a = collection.find_one({"id": twitter_id})
	return bool(a)


def get_tweets(filters={}, connection=None):
	if connection is None:
	    db = get_db("teenspirit")
	else:
	    db = connection
	collection = db["tweets"]
	result = collection.find(filters)
	return [doc for doc in result]


if __name__ == "__main__":
	add_to_mongo({"id": 55555555555555555})
	is_exists(55555555555555555)
	is_exists(11111111111111111)
