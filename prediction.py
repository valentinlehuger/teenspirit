from pymongo import MongoClient
import pandas as pd
import numpy as np
from scipy.stats import entropy
from pandas.io.json import json_normalize
import datetime
import warnings
import re
import json
warnings.simplefilter(action = "ignore", category = RuntimeWarning)

client = MongoClient("mongodb://romain:teenspirit@ds011462.mlab.com:11462/teenspirit")
db = client['teenspirit']

coll = db.tweets #db.users

mongo_out = list(coll.find({},{'retweeted_status':0}))
for i in range(len(mongo_out)):
    if 'urls' in list(mongo_out[i].keys()):
        mongo_out[i]['has_urls'] = 1
        del mongo_out[i]['urls']
    else:
        mongo_out[i]['has_urls'] = 0
df = json_normalize(mongo_out)
del mongo_out

path = '/home/romain/Documents/Github/teenspirit/'
#==============================================================================
# path = '/home/romain/Documents/BitBucket/DataForGood/teenspirit/teenspirit/'
# 
# hashtags = ['mort','mourir','suicide']
# df_tmp = {}
# col = None
# for hashtag in hashtags:
#     json_data=open(path+hashtag+".json").read()
#     data = json.loads(json_data)
#     df_tmp[hashtag] = json_normalize(data)
#     if col is None:
#         col = list(df_tmp[hashtag].columns)
#     else:
#         col = list(set(col) & set(df_tmp[hashtag].columns))
# 
# df = None
# for hashtag in hashtags:
#     if df is None:
#         df = df_tmp[hashtag][col]
#     else:
#         df = pd.concat([df,df_tmp[hashtag][col]])
#==============================================================================


def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    ma = np.convolve(interval, window, 'full')
    ma = ma[:len(interval)]
    ma[0] = interval[0]
    return ma

def timeSerieFeatures(x,M):
    mn = np.mean(x)
    std = np.std(x)
    ent = entropy(x)
    mean_momentum = np.mean(x-movingaverage(x,M))
    return mn, std, ent, mean_momentum


users = df[['user.id']].drop_duplicates()
users['user.id'] = list(map(str,users['user.id']))
df['user.id'] = list(map(str,df['user.id']))
df['datetime'] = list(map(lambda x: datetime.datetime.strptime(x,"%a %b %d %H:%M:%S %z %Y"),df['created_at']))
df['day'] = list(map(lambda x: datetime.datetime.date(x),df['datetime']))

timeline = pd.date_range(df['day'].min(),df['day'].max())
# convert to dataframe to then merge each variable on this timeline and 
# compute time serie
timeline = pd.DataFrame({'day':list(map(lambda x: datetime.datetime.date(x),timeline))})

def timeseriename(x):
    return [x+"_mn",x+"_std",x+"_ent",x+"_mn_mom"]
    
col = ['user.id','day']
col.extend(timeseriename('volume'))
col.extend(timeseriename('insomnia'))
col.extend(timeseriename('fr_retweet'))
col.extend(timeseriename('fr_urls'))
col.extend(timeseriename('fr_question'))
features = pd.DataFrame(columns = col)

features['user.id'] = users['user.id']
features['day'] = timeline['day'].max() # ? la date d'aujourd'hui ? de sa dernière venu ? de la date d'aujourdhui et depuis combien de temps on l'a pas vu ? 

#==============================================================================
# Engagement
#==============================================================================
"""
o   (DONE) Volume : normalized number of posts per day made by the user ;
o   Proportion of reply posts (@-replies) from a user per day à level of social 
    interaction with other users ;
o   (DONE) Fraction of retweets from a user per day à participation in information 
    sharing with followers ;
o   (DONE) Proportion of links (urls) shared by each user over a day ;
o   (DONE) Fraction of question-centric posts from a user in a day à tendency to seek 
    and derive informational benefits from the community  (présence d’un point 
    d’interrogation);
o   (DONE) Insomnia index = normalized difference in number of posting made between 
    night window and day window on a given day à pattern of posting during the 
    course of a day. Moments of day of activity. Night window = 9PM – 6AM vs 
    day window.
"""

### Volume
vol = df.groupby(['user.id','day'])['id'].count().reset_index()

for user in users['user.id']:
    x = vol[['id','day']][vol['user.id']==user]
    x = pd.merge(timeline,x,how='left')
    x = x.fillna(0)
    features.loc[features['user.id']==user,timeseriename('volume')] = timeSerieFeatures(list(x['id']),7)

### Fraction of retweets
# retweeted : is this a retweet
# The fraction of retweets from a user per day, signaling how
# she participates in information sharing with her followers
df.loc[df.index,'is_retweet'] = np.repeat(0,len(df))
df.loc[df['retweet_count']>0,'is_retweet']=1
retweet_sum = df.groupby(['user.id','day'])['is_retweet'].sum().reset_index()
retweet_count = df.groupby(['user.id','day'])['retweeted'].count().reset_index()
retweet = pd.merge(retweet_sum,retweet_count,on=['user.id','day'])
retweet['fraction'] = retweet['is_retweet']/retweet['retweeted']

for user in users['user.id']:
    x = retweet[['fraction','day']][retweet['user.id']==user]
    x = pd.merge(timeline,x,how='left')
    x = x.fillna(0)
    features.loc[features['user.id']==user,timeseriename('fr_retweet')] = timeSerieFeatures(list(x['fraction']),7)

### Proportion of links
urls_sum = df.groupby(['user.id','day'])['has_urls'].sum().reset_index()
urls_count = df.groupby(['user.id','day'])['has_urls'].count().reset_index()
urls = pd.merge(urls_sum,urls_count,on=['user.id','day'])
urls['fraction'] = urls['has_urls_x']/urls['has_urls_y']

for user in users['user.id']:
    x = retweet[['fraction','day']][retweet['user.id']==user]
    x = pd.merge(timeline,x,how='left')
    x = x.fillna(0)
    features.loc[features['user.id']==user,timeseriename('fr_urls')] = timeSerieFeatures(list(x['fraction']),7)

### Fraction of question-centric
def isQuestion(x):
    tmp = re.search('\?',x)
    if tmp is None:
        return 0
    else:
        return 1

df['question'] = list(map(isQuestion,df['text']))
question_sum = df.groupby(['user.id','day'])['question'].sum().reset_index()
question_count = df.groupby(['user.id','day'])['question'].count().reset_index()
question = pd.merge(question_sum,question_count,on=['user.id','day'])
question['fraction'] = question['question_x']/question['question_y']

for user in users['user.id']:
    x = retweet[['fraction','day']][retweet['user.id']==user]
    x = pd.merge(timeline,x,how='left')
    x = x.fillna(0)
    features.loc[features['user.id']==user,timeseriename('fr_question')] = timeSerieFeatures(list(x['fraction']),7)

### Insomnia index
df['hour'] = list(map(lambda x: x.hour,df['datetime']))
df['hour_window'] = list(map(lambda x: 'day' if 6<=x<21 else 'night',df['hour']))

user_insomnia = df.groupby(['user.id','day','hour_window'])['id'].count().unstack()
user_insomnia = user_insomnia.rename(columns={'day':'day_window','night':'night_window'}).reset_index()
user_insomnia = user_insomnia.fillna(0)
user_insomnia['insomnia'] = (user_insomnia['night_window']-user_insomnia['day_window'])/(user_insomnia['night_window']+user_insomnia['day_window'])

# user_insomnia['insomnia'] is between -1 and 1 -> scale on 0 - 1 (otherwise entropy = inf)
user_insomnia['insomnia'] = (user_insomnia['insomnia']+1)/2

for user in users['user.id']:
    x = user_insomnia[['insomnia','day']][user_insomnia['user.id']==user]
    x = pd.merge(timeline,x,how='left')
    x = x.fillna(0)
    features.loc[features['user.id']==user,timeseriename('insomnia')] = timeSerieFeatures(list(x['insomnia']),7)




#==============================================================================
# Egocentric Social Graph
#==============================================================================
"""
o   Node properties :
    - number of followers or inlinks of a user at a given day;
    - number of user followees or outlinks.
o   Dyadic properties (interaction with another user @-replies) :
	-  reciprocity : mean number of @-replies from u to v / number of @-replies 
     from v to u ;
	- prestige ratio : mean over v of 
     ( number of @-replies to u (u targeted) / number of @-replies to v where v 
     is a user with whom u has a history )
o   Network properties (entire egocentric network @-replies exchanges) :
    - graph density : number of edges (u to v and v to u) / number of nodes (u to v)
    - clustering coefficient : average probability that two neighbors of u are 
    neighbors of each other ;
    - size of two-hop neighborhood : number of neighbors + number of neighbors 
    of neighbors ;
    - embeddedness : number of neighbors u INTER neighbors v / number of neighbors 
    u DISTINCT UNION v ;
    - number of ego components : A DETAILLER

Undirected network. Edge between u and v = at least one @-reply exchange 
(from u to v and from v to u on a given day)
"""

#==============================================================================
# Emotion
#==============================================================================
"""
o   LIWC
o   ANEW
    - activation = degree of physical intensity in an emotion (Terrified > scared)
    - dominance = degree of control in an emotion (anger : dominant, fear : 
    submissive)
"""


#==============================================================================
# Linguistic Style
#==============================================================================
"""
o   LIWC. Characterize linguistic styles
    - articles, auxilary verbs, conjunctions, adverbs, personal pronouns, 
    negation etc.
"""

#==============================================================================
# Depression Language
#==============================================================================
"""
o   (a) usage of depression-related terms → define a lexicon with drepression 
    terms / symptoms
    Yahoo! “Mental Health”
	+ question / answer pairs ??? 
o   (b) popular antidepressants in the treatment of clinical depression
Wikipedia page ‘list of antidepressants’ > lexicon of drugs name.
"""

#==============================================================================
# User descriptors
#==============================================================================
users_context = df[['datetime','user.id','user.friends_count','user.followers_count']].drop_duplicates()
users_context['user.id'] = list(map(str,users_context['user.id']))
users_context = users_context.loc[users_context.groupby(['user.id'])['datetime'].idxmax()]
del users_context['datetime']
users_context = users_context.rename(columns={'user.friends_count':'friends_count',
                                              'user.followers_count':'followers_count'})
features = pd.merge(features,users_context,on='user.id')



features['day'] = list(map(str,features['day']))
features_json = features.to_dict(orient='records')
with open(path+"features.json", 'w') as outputfile:
    json.dump(features_json, outputfile)
    print("dump result into features.json")