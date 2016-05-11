# @Author: valentin
# @Date:   2016-05-11T22:28:26+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-11T22:29:19+02:00


def userTimeline(userId, max_id=None, rec=100, api):
	""" Returns other tweets from a user. """
	print rec
	if rec <= 0:
		return []

	tweets = api.GetUserTimeline(userId, max_id=max_id)
	print type(tweets)
	max_id = str(int(min([x.id for x in tweets])) - 1)
	print max_id
	return tweets + userDeepDive(userId, max_id, rec=rec-1)
