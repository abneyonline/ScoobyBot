import cv2 as cv
import tweepy
import os
import sys
from numpy import sqrt, log, cos, pi, random

# Set Up Media to Pull From
seriesMap = {'WhereAreYou':'Scooby-Doo Where are You!',
'ScoobyDooShow':'The Scooby-Doo Show'}
lexicon = os.environ['SCOOBYLEXICON']

# Determine Exact Episode
series = random.choice(os.listdir(lexicon))
episode = random.choice(os.listdir(os.path.join(lexicon, series)))
fullPath = os.path.join(lexicon, series, episode)
# fullPath = os.path.join(lexicon, 'WhereAreYou', 'S01E01 - What A Night For A Knight.mp4')

# Open video file
cap = cv.VideoCapture(fullPath)

# Find the target frame
length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
targetFrame = random.randint(0, length-1)

# Retrieve the target frame
cap.set(cv.CAP_PROP_POS_FRAMES, targetFrame)
ret, frame = cap.read()
gray = cv.cvtColor(frame, 0)
# Print the target frame to file
cv.imwrite('temp.png',gray)
# Cleanup
cap.release()
#cv.destroyAllWindows()

# Retrieve @BotScooby's oauth information from environment variables.
auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)

if len(sys.argv) is not 1:
    print(seriesMap[series] + " " + episode[:-4])
else:
    api.update_with_media('temp.png', seriesMap[series] + " " + episode[:-4] + ' #ScoobyDoo')
