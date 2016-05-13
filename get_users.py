from bluebirdlib.connection import get_api
from bluebirdlib.user import userTimeline
from bluebirdlib.data import add_json_object
from sys import argv
import pprint


#User ids list to fill
user_ids = ["2637627982"]


if __name__ == "__main__":
    max_request = 100

    if not user_ids:
        raise Exception("Need user ids")
    if  len(user_ids) > max_request:
        raise Exception("Too much user ids")

    filename = None
    if len(argv) > 1:
        filename = argv[1]

    api = get_api("./")

    for uid in user_ids:
        tweets = map(lambda x: x.AsDict(), userTimeline(uid, api, rec=max_request/len(user_ids)))
        if filename:
            if add_json_object({uid: tweets}, filename):
                print("[OK] Add %s tweets into %s" % (uid, filename))
            else:
                print("[ERROR] Can't add %s tweets into %s" % (uid, filename))
        else:
            pprint.PrettyPrinter(indent=2).pprint(tweets)
