import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Create a Sentiment List
polarityList = []

#[OPTIONAL] Subjectivity
subjectivityList = []

#Get Sentiment Data
for tweet in tweetData:
	tweetblob = TextBlob(tweet["text"])
	polarityList.append(tweetblob.polarity)

	#[OPTIONAL] Subjectivity
	subjectivityList.append(tweetblob.subjectivity)

print(polarityList)
print(subjectivityList)
