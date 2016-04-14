# coding: utf-8
import twitter



keys = [[x.strip() for x in raw_input().split(':')][1] for i in range(4)]


api = twitter.Api(consumer_key=keys[0],
                      consumer_secret=keys[1],
                      access_token_key=keys[2],
                      access_token_secret=keys[3])


def getTweetFromHashTag(word):
    search = '#' + word

    l =  api.GetSearch(search, result_type="recent", count=1000)
    for e in l:
        print "=" * 50
        print e.user.name
        print e.id
        print e.text
        print e.created_at
        if e.place:
            print e.place["full_name"]

    return l


def userDeepDive(userId):
    """ Returns other tweets from a user. """
    return api.GetUserTimeline(userId)


if __name__ == "__main__":
    l = getTweetFromHashTag("deprime")
    for status in l:
        tl = userDeepDive(status.user.id) 
        print "=================" * 3
        print "=================" * 3
        print "=================" * 3
        for e in tl:
            print "=" * 50
            print e.user.name
            print e.id
            print e.text
            print e.created_at
            if e.place:
                print e.place["full_name"]        
