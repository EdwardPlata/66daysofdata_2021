from psaw import PushshiftAPI
import datetime

api=pushshiftAPI()

start_time = int(datetime.datetime(21,1,31).timestamp())
submissions = api.search_submissions(after=start_time,
					subreddit ='wallstreetbets',
					filter =['url','author','title','subreddit']
for submission in submissions:
	print(sbmission.url)

#Add ways to check if a stock is metion to measure populatirty as well as connection to my sql server	

