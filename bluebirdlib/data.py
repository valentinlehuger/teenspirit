# @Author: valentin
# @Date:   2016-05-14T01:46:03+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-17T00:29:03+02:00

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


def add_to_mongo(object, database="teenspirit", collection="tweets", connection=None):
	if connection is None:
	    db = get_db(database)
	else:
	    db = connection
	collection = db[collection]
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


def get_tweets(filters={}, limit=0, connection=None):
        if connection is None:
                db = get_db("teenspirit")
        else:
                db = connection
        collection = db["tweets"]
        result = collection.find(filters, limit=limit)
        return [doc for doc in result]


def update_tweet(filter, query, connection=None):
    if connection is None:
        db = get_db("teenspirit")
    else:
        db = connection
    collection = db["tweets"]
    result = collection.update(filter, {"$set": query})
    return result

def get_distinct_users(connection=None):
    if connection is None:
        db = get_db("teenspirit")
    else:
        db = connection
    collection = db["tweets"]
    result = collection.distinct("user")
    return map(lambda x: x["id"], result)


def get_users(filters={}, limit=0, connection=None):
    if connection is None:
        db = get_db("teenspirit")
    else:
        db = connection
    collection = db["users"]
    result = collection.find(filters, limit=limit)
    return result

def update_user(filter={}, query={}, connection=None):
    if connection is None:
        db = get_db("teenspirit")
    else:
        db = connection
    collection = db["users"]
    print "filter: ", filter
    print "query: ", query
    result = collection.update(filter, query)
    print "result: ", result
    return result


if __name__ == "__main__":
	# add_to_mongo({"id": 55555555555555555})
	# is_exists(55555555555555555)
	# is_exists(11111111111111111)
    print get_distinct_users()
