# Import opencv
import cv2 

# Import uuid
import uuid

# Import Operating System
import os
# Import time
import time

labels = ['damaged', 'undamaged']  #the different Identifiers
number_imgs = 100  #number of images we want to collect
IMAGES_PATH = os.path.join('solarAI', 'images', 'collectedimages')
#print(IMAGES_PATH)

for label in labels:
    path = os.path.join(IMAGES_PATH, label)

for label in labels:
    cap = cv2.VideoCapture(0) #connects to camera, idk what number the one we're using is
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

LABELIMG_PATH = os.path.join('SolarAI', 'labelimg')
