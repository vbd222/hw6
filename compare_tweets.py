import json
"""
Sadly, didn't do pre- and post-debate.  So doing two runs.
Checking to see how much overlap - may have to wait until morning.
"""

with open('sinema_tweets_run437pm.json') as fp:
    tweets = json.load(fp)

with open('sinema_tweets.json') as fp:
    tweets2 = json.load(fp)
    
count = 0
for t in tweets:
    if t in tweets2:
        count += 1
print('Number of repeated Sinema tweets:', count)

with open('mcsally_tweets_run437pm.json') as fp:
    tweets = json.load(fp)

with open('mcsally_tweets.json') as fp:
    tweets2 = json.load(fp)

count = 0
for t in tweets:
    if t in tweets2:
        count += 1
print('Number of repeated McSally tweets:', count)

