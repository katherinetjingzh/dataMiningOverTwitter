# Advanced Uses of Streaming APIs

# Streaming APIs Overview

# Twitter offers several streaming endpoints, each customized to certain use cases.
# 1. Public streams : Streams of the public data flowing through Twitter
# 2. User streams: Single-user streams, containing roughly all of the data 
# corresponding with a single user's view of Twitter.
# 3. Site sterams: The multi-user version of user streams. Site 


# Set different parameters to define what data to request.
# For example, track certain tweets by specifying keywords or location or 
# language.
# iterator = twitter_stream.statuses.filter(track="Google", language="en")