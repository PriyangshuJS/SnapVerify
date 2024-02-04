import Sign_up as su
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
import os

# Initialize Firebase
# cred = credentials.Certificate("C:/Users/swast/Downloads/snapverify-e7124-firebase-adminsdk-wvdy8-c27bd424f8.json")
# if not firebase_admin._apps:
#     firebase_admin.initialize_app(cred)
# db = firestore.client()


def parse_dir():
    file_path = []
    directory = 'image_folder'
    files = [f for f in os.listdir(directory) if f.lower().endswith(('.txt'))]
    file_path.append(directory+'/'+files[0])
    return file_path




# Function to post an array along with user data to the "users" collection
def post_array_to_users(array, db, uid):
    try:
        # Assuming the user data already exists in the database with the given UID
        user_ref = db.collection("users").document(uid)
        # Update the user document to include the array field
        user_ref.update({
            'array': array.tolist()  # Convert NumPy array to Python list
        })

        print("Array posted successfully to the user document")
    except Exception as e:
        print(f"Error posting array to user document: {e}")

# Example usage:
# Assuming 'output_list' is the face encodings obtained from face_recognition






def master(db):
    files = parse_dir()
    print(files)
    file = open(files[0], 'r')
    uid = file.read()
    file.close()
    output_list = su.master()
    post_array_to_users(output_list, db, uid)

