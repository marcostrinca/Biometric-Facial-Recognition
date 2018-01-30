import argparse, os, sys, time
import numpy as np
from scipy import ndimage

# video  and utils
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import face_detection_utilities as fdu
import cv2

from billiard import Process, forking_enable

def cam():
	vc = cv2.VideoCapture(0) #modify 0/1 to toggle between USB and internal camera
	while True:
		junk,image = vc.read()
		cv2.imshow("test",image)
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

##### main
def main():
	print('starting')

	forking_enable(0) # Is all you need!
	camProcess = Process(target=cam, args=(0,))
	camProcess.start()

if __name__ == '__main__':
	main()
	cam()