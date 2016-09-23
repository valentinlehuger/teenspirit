from bluebirdlib.data import add_to_mongo
from bluebirdlib.data import is_exists
from bluebirdlib.tasks.fetch_twitter import FetchTwitterTask
from bluebirdlib.user import userTimeline


class GetUserTweetsTask(FetchTwitterTask):

    def run(self, params):
        user = params.get("user", None)
        if not user:
            raise Exception("User id not provide.")

        tweets = [x.AsDict() for x in userTimeline(user, self.api, rec=1)]
        [add_to_mongo(x) if not is_exists(x["id"]) else None for x in tweets]
        return 0
