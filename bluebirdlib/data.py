# @Author: valentin
# @Date:   2016-05-14T01:46:03+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-16T21:19:01+02:00

from pymongo import MongoClient
import os
import json

def get_db(database, ip="localhost", port=27017, mongolab=False):
    if mongolab:
        up = get_user_password()
        if up is None:
            print "Error to get db because file mongolab_register not define."
            return None
        else:
            return MongoClient('mongodb://' + up["user"] + ':' + up["password"] + '@%s:%d/' % (ip, port) + database)[database] or None
    else:
        client = MongoClient(ip, port)
        return client[database] or None


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
	post_id = collection.insert(object)
	return post_id



if __name__ == "__main__":
	add_to_mongo({"test": 1})
