import os
import json


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

if __name__ == "__main__":
    add_json_object({"test1": 1}, "test.json")
    add_json_object({"test2": 2}, "test.json")
