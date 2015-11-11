from twitter import *

config = {}
execfile("config.py", config)

# for keys, values in config.items():
# 	print(keys)
# 	print(values)

# Create twitter API object
twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"],
					config["consumer_key"], config["consumer_secret"]))

# query  = twitter.search.tweets(q='harry potter');

source = "tjingzh"
target = "ideoforms"

result = twitter.friendships.show(source_screen_name = source,
								  target_screen_name = target)
print result

following = result["relationship"]["target"]["following"]
follows   = result["relationship"]["target"]["followed_by"]

print "%s following %s : %s" % (source, target, follows)
print "%s following %s : %s" % (target, source, following)			  
# query = twitter.friends.id(screen_name = username)

# print "found %d friends" % (len(query["ids"]))

