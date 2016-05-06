# coding: utf-8
# @Author: valentin
# @Date:   2016-04-21T14:32:53+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-04-21T16:13:41+02:00

import twitter
import json


keys = [[x.strip() for x in raw_input().split(':')][1] for i in range(4)]


api = twitter.Api(consumer_key=keys[0],
                      consumer_secret=keys[1],
                      access_token_key=keys[2],
                      access_token_secret=keys[3])


def getTweetFromHashTag(word):
    search = '#' + word

    l =  api.GetSearch(search, result_type="recent", count=1000)
    # for e in l:
        # print "=" * 50
        # print e.user.name
        # print e.id
        # print e.text
        # print e.created_at
        # if e.place:
        #     print e.place["full_name"]

    return l


def userDeepDive(userId, max_id=None, rec=100):
	""" Returns other tweets from a user. """
	print rec
	if rec <= 0:
		return []

	tweets = api.GetUserTimeline(userId, max_id=max_id)
	print type(tweets)
	max_id = str(int(min([x.id for x in tweets])) - 1)
	print max_id
	return tweets + userDeepDive(userId, max_id, rec=rec-1)


if __name__ == "__main__":

	dataset = list()
	profiles = ["drunktolive", "lesjolismaux"]
	x = 2
	for profile in profiles:
		for status in userDeepDive(api.GetUser(screen_name=profile).id, rec=150):
			tweet = {
				"id": status.id,
				"datetime": status.created_at,
				"user": {
					"id": status.user.id,
					"name": status.user.name,
					"screen_name": status.user.screen_name,
					"created_at": status.user.created_at
				},
				"text": status.text
			}
			dataset.append(tweet)

		with open("dataset%d.json" % x, 'w') as dsf:
			json.dump(dataset, dsf)
		x += 1

    # l = getTweetFromHashTag("deprime")
    # for status in l:
    # 	print status.user
    #     print "=================" * 3
    #     print "=================" * 3
    #     print "=================" * 3
    #     for e in tl:
    #         print "=" * 50
    #         print e.user.name
    #         print e.id
    #         print e.text
    #         print e.created_at
    #         if e.place:
    #             print e.place["full_name"]
