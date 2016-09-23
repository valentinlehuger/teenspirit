from bluebirdlib.tasks.fetch_twitter import FetchTwitterTask
from bluebirdlib.status import getTweetFromHashTag
from bluebirdlib.data import add_to_mongo
from bluebirdlib.data import is_exists


class GetHashTagTweetsTask(FetchTwitterTask):

    def run(self, params):
        search = params.get("search", None)
        if not search:
            raise Exception("Search not provide.")
        tweets = [x.AsDict() for x in getTweetFromHashTag(search, self.api)]
        [add_to_mongo(x) if not is_exists(x["id"]) else None for x in tweets]
        return 0
