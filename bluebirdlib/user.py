# @Author: valentin
# @Date:   2016-05-11T22:28:26+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-11T23:15:20+02:00

from bluebirdlib.data import get_users, get_tweets, update_user


def userTimeline(userId, api, max_id=None, rec=20):
    """ Returns other tweets from a user. """
    if rec <= 0:
        return []

    tweets = api.GetUserTimeline(userId, max_id=max_id)
    if not tweets:
        return []
    max_id = str(int(min([x.id for x in tweets])) - 1)
    return tweets + userTimeline(userId, api, max_id, rec=rec-1)


def get_next_users_to_display(limit=50, connection=None):
    filters = {"controls": []}
    return [x for x in get_users(filters, limit=limit, connection=connection)]


def add_control_to_user(user_id, control, connection=None):
    filters = {"user_id": user_id}
    query = {
        "$push": {
            "controls": control
        }
    }
    print "in add control"
    return update_user(filters, query, connection=connection)


if __name__ == '__main__':
    users = get_next_users_to_display()
    X = get_tweets(filters={"user.id": {"$in": map(lambda user: user["user_id"], users)}})
    print len(X)
