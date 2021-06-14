import tweepy, logging
# assign the values accordingly 

def TweetAPI(consumer_key,consumer_secret,access_token,access_token_secret):

	if consumer_key == None or consumer_secret == None or access_token == None or access_token_secret == None:
		raise ValueError(f'{sum([bool(x) for x in [consumer_key,consumer_secret,access_token,access_token_secret]])} tokens missing')
	  
	# authorization of consumer key and consumer secret 
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
		  
		# set access to user's access key and access secret  
		auth.set_access_token(access_token, access_token_secret) 
		api = tweepy.API(auth) 
		return api
	except Exception as e:
		logging.error(e)
	  
# calling the api  

if __name__ == "__main__":
	logging.info("This is TweetAPI method that returns a twitter api.\n Get your consumer_key, consumer_secret, access_token and access_token_secret from https://developer.twitter.com/en/portal/dashboard")

