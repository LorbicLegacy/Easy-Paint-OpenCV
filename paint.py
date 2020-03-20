import math
import numpy as np 
import cv2


drawing = False # True if mouse is pressed
ix, iy = -1,-1
img = cv2.imread("background.png")
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

def nothing(x):
	pass

# mouse callback function
def draw(event,x,y,flags,param):
	global ix,iy,drawing
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			if s == 3:
				cv2.circle(img,(x,y),5,(b,g,r),-1)
	elif event == cv2.EVENT_LBUTTONUP:
		if drawing == True:
			if s == 0:
				cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),5)
			elif s == 1:
				cv2.circle(img,(int((ix+x)/2),int((iy+y)/2)),int(math.sqrt(((ix-x)**2)+((iy-y)**2))),(b,g,r),5)
			elif s == 2:
				cv2.line(img,(ix,iy),(x,y),(b,g,r),5)

		drawing = False

#load an image
# cv2.imshow("Easy Paint by Vikas Patel",image)

#create trackbars
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

#create trackbar for drawing line
cv2.createTrackbar('Select','image',0,3,nothing)



cv2.setMouseCallback('image',draw)

while(1):
	cv2.imshow('image',img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

	#get current positions of four trackbars
	r = cv2.getTrackbarPos('R','image')
	g = cv2.getTrackbarPos('G','image')
	b = cv2.getTrackbarPos('B','image')
	s = cv2.getTrackbarPos('Select','image')







cv2.destroyAllWindows()