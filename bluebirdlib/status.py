# @Author: valentin
# @Date:   2016-05-11T22:23:43+02:00
# @Last modified by:   valentin
# @Last modified time: 2016-05-11T22:55:34+02:00


def getTweetFromHashTag(search, api):
    search = '#' + search
    l =  api.GetSearch(search, result_type="recent", count=1000)
    return l
