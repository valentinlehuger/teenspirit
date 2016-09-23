from mrq.job import queue_jobs
from mrq.job import queue_job
from mrq.task import Task
from bluebirdlib.data import get_distinct_users
from hashtags import HASHTAGS

class SchedulerTask(Task):

    def run(self, params):
        users = [{"user": x} for x in get_distinct_users()]
        print "Queue users"
        queue_jobs("bluebirdlib.tasks.GetUserTweets", users, queue="tweets")
        hts = [{"search": x} for x in HASHTAGS]
        print "Queue hashtags"
        queue_jobs("bluebirdlib.tasks.getHashTagTweets", hts, queue="tweets")
        print "Queue scheduler"
        queue_job("bluebirdlib.tasks.Scheduler", {}, queue="tweets")
        return 0
