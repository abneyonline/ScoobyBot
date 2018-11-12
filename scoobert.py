import cv2 as cv
from numpy import sqrt, log, cos, pi, random

cap = cv.VideoCapture('newbert.mp4')

length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
targetFrame = random.randint(0, length-1)
cap.set(cv.CAP_PROP_POS_FRAMES, targetFrame)
ret, frame = cap.read()
gray = cv.cvtColor(frame, 0)
cv.imwrite('temp.png',gray)
cap.release()
cv.destroyAllWindows()

