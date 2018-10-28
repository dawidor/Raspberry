import cv2, os
import numpy as np
from PIL import Image

def convertToRGB(img):     
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.jpg')]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    # return the images list and labels list
    return images, labels

#load test iamge
test1 = cv2.imread('img1.jpg')
#convert the test image to gray image as opencv face detector expects gray images 
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)




face_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_eye.xml')




#let's detect multiscale (some images may be closer to camera than others) images 
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);  

#print the number of faces found 

print('Faces found: ', len(faces));

#let's detect multiscale (some images may be closer to camera than others) images 
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);  
 
 #print the number of faces found 
print('Faces found: ', len(faces))



# Path to the Yale Dataset
path = 'data' 
# The folder yalefaces is in the same folder as this python script
# Call the get_images_and_labels function and get the face images and the 
# corresponding labels
images, labels = get_images_and_labels(path)

recognizer = cv2.face.LBPHFaceRecognizer_create() 
recognizer.train(images, np.array(labels))
# Append the images with the extension .sad into image_paths
image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg2')]
for image_path in image_paths:
    predict_image_pil = Image.open(image_path).convert('L')
    predict_image = np.array(predict_image_pil, 'uint8')

faces = faceCascade.detectMultiScale(predict_image)
for (x, y, w, h) in faces:
    nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
    nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
    if nbr_actual == nbr_predicted:
        print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
    else:
        print "{} is Incorrectly Recognized as {}".format(nbr_actual, nbr_predicted)
    cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
    cv2.waitKey(1000)

#cv2.imshow('Test Imag', gray_img) 
cv2.waitKey(0) 
                
cv2.destroyAllWindows()
            

