import face_recognition
import cv2

# imagePath = 'sud.jpg'
# img = cv2.imread(imagePath)

def face_locs(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )
    return face

def detect_multiple_faces(img):
    face = face_locs(img)
    if face.shape[0] != 1:
        raise ValueError("Multiple faces detected")
    
def face_embed(img):
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    return face_encodings

def face_compare(array_old, array_new):
    results = face_recognition.compare_faces(array_old, array_new)
    print(results)
    
def master_method(img, array):
    detect_multiple_faces(img)
    face_encodings = face_embed(img)
    face_compare(array, face_encodings)

master_method(img, array)