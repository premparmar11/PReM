#import modules cv2(open cv) & date-time
import cv2
import datetime

#cascade xml file and intialization
face_cascade = cv2.CascadeClassifier('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37\\cv2\\data\\haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37\\cv2\\data\\haarcascade_smile.xml')

#reference time (will use ahead)
c1 = datetime.datetime(1999,9,11)
print(c1)

#loading a cascade library and checking (is it loaded or not?)
test=face_cascade.load('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37\\cv2\\data\\haarcascade_frontalface_default.xml')
test1=smile_cascade.load('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37\\cv2\\data\\haarcascade_smile.xml')
print(test) #expected to be a TRUE
print(test1)

#default static image loading
img= cv2.imread("notsmile.jpg")

#this is used for resizing image
#img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))

#display default image
cv2.imshow("",img)

#for a 2sec, displays image on screen
cv2.waitKey(2000)

#close or destroy all windows
cv2.destroyAllWindows()

#convert image from one color space to another (16 bit to 8 bit)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect input image(diff size) and return list of recteangles
#diff for diff cascade
faces = face_cascade.detectMultiScale(gray_img,1.05,5)

print(type(faces))
print(faces)

#returned list of rectangles in faces and drawing rectangle usinf for loop
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)

faces = smile_cascade.detectMultiScale(gray_img,1.7,3)
print(faces)

#smile is not there , then empty is tuple/list :- length is ZERO then no smile
#pop up a message or jokes for a smile
#if we use here timer/stopwatch then after exceeding 15-20 min ,
#A person not smiled then diff jokes appears on screen
if len(faces) == 0 :
    print("not smiling")
    import ctypes  # An included library with Python install.   
    ctypes.windll.user32.MessageBoxW(0,"any jokes", "Smile Please", 1)

#same as face detection :- smile detection
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)

#display image after detection
cv2.imshow("",img)
