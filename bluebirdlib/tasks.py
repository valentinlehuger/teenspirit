from mrq.task import Task
from bluebirdlib.connection import get_api
from bluebirdlib.status import getTweetFromHashTag
from bluebirdlib.user import userTimeline
from bluebirdlib.data import add_to_mongo, is_exists

import pprint

class FetchTwitterTask(Task):

    def __init__(self):
        try:
            self.api = get_api("./")
        except:
            raise Exception("Impossible to get the api")


class GetHashTagTweets(FetchTwitterTask):

    def run(self, params):
        search = params.get("search", None)
        if not search:
            raise Exception("Search not provide.")

        tweets = map(lambda x: x.AsDict(), getTweetFromHashTag(search, self.api))
        pprint.PrettyPrinter(indent=2).pprint(tweets)
        map(lambda x: add_to_mongo(x) if not is_exists(x["id"]) else None, tweets)
        return 0


class GetUserTweets(FetchTwitterTask):

    def run(self, params):
        user = params.get("user", None)
        if not user:
            raise Exception("User id not provide.")

        tweets = map(lambda x: x.AsDict(), userTimeline(user, self.api, rec=1))
        map(lambda x: add_to_mongo(x) if not is_exists(x["id"]) else None, tweets)
        return 0
