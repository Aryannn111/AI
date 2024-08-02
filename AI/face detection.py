import cv2 # import the opencv lib 

#function to draw boundaries (rectangle)
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    #convert the image to greyscale 
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect feature in the greyscale ,provided classifier
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = [] # initialize list to store coords of detect feature
    for (x, y, w, h) in features:# iterate through all detect feature 
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2) # craete rectangle
        # put text 
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h] #update coords 

    return coords # return the coords 

# function to detect faces (nose , eyes ,mouth)
def detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade):
    #define colors 
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
    # detect faces in the image 
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")
    # if a face is detect (4 elements)
    if len(coords)==4:
        #extract the region of interest (ROI) corresponding to the detected face
        roi_img = img[coords[1]:coords[1]+coords[3], coords[0]:coords[0]+coords[2]] #[1,3] vertiaclly y+h [0,2] x+w ,horizentally 
        # detect eyes within the face (ROI)
        coords = draw_boundary(roi_img, eyeCascade, 1.1, 12, color['red'], "Eye")
        # detect nose within the face (ROI)
        coords = draw_boundary(roi_img, noseCascade, 1.1, 4, color['green'], "Nose")
        # detect eyes within the face (ROI)
        coords = draw_boundary(roi_img, mouthCascade, 1.1, 20, color['white'], "Mouth")
    return img # return the image with drawn boundaries

# load pre trained haar cascade classifier for face eyes mouth nose detection
faceCascade = cv2.CascadeClassifier('face_default.xml')
eyesCascade = cv2.CascadeClassifier('eye.xml')
noseCascade = cv2.CascadeClassifier('nose.xml')
mouthCascade = cv2.CascadeClassifier('Mouth.xml')

# capture video from the default camera
video_capture = cv2.VideoCapture(0)

# create loop for capture frames from vid 
while True:
    # read a frame 
    _, img = video_capture.read()
    # detect feature 
    img = detect(img, faceCascade, eyesCascade, noseCascade, mouthCascade)
    # display the annotate frame in a window
    cv2.imshow("face detection", img)
    # break the loop when click a
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
    
# release the video capture 
video_capture.release()
# destroy all opencv window
cv2.destroyAllWindows()