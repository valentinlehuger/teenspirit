from mrq.task import Task
from bluebirdlib.connection import get_api


class FetchTwitterTask(Task):

    def __init__(self):
        try:
            self.api = get_api("./")
        except:
            raise Exception("Impossible to get the api")
