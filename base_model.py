import face_recognition
import cv2

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
    return face

def error_detection(img):
    face = detect_multiple_faces(img)
    if face.shape[0] != 1:
        raise ValueError("Multiple faces detected")
    
def face_embed(img):
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    return face_encodings