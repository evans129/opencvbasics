import cv2
#print("allgood")
img=cv2.imread("/Users/devanshkumar/Downloads/imopencv.jpg",0)
cv2.imshow("output",img)
cv2.waitKey(2000)
#cap=cv2.VideoCapture("/Users/devanshkumar/Downloads/vidopen.mp4")
#cap=cv2.VideoCapture(0)
#cap.set(3,1080)
#cap.set(4,480)
#while cap.isOpened():
    #success,img=cap.read()
    #cv2.imshow("video",img)
    #if cv2.waitKey(1) & 0xFF==ord('q'):
    # break