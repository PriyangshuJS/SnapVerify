import firebase_admin
from firebase_admin import credentials, firestore
from PIL import Image
import requests
from io import BytesIO
import os
from urllib.parse import urlparse
import output as op

# Initialize Firebase
cred1 = credentials.Certificate("C:/Users/swast/Downloads/snapverify-e7124-firebase-adminsdk-wvdy8-c27bd424f8.json")
firebase_admin.initialize_app(cred1)
db = firestore.client()

def display_image_from_url(image_url, uid, save_folder):
    if image_url:  # Check if image_url is not empty
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content
            img = Image.open(BytesIO(image_data))
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
            filename = os.path.basename(urlparse(image_url).path)
            save_path = os.path.join(save_folder, filename)
            img.save(save_path)
            print(f"Image saved to: {save_path}")
            img.show()
            # Write UID to a text file in the same folder
            uid_file_path = os.path.join(save_folder, f"{uid}.txt")
            with open(uid_file_path, 'w') as uid_file:
                uid_file.write(uid)
                print(f"UID saved to: {uid_file_path}")
        else:
            print("Failed to fetch image from URL:", image_url)
    else:
        print("Empty image URL provided.")

def get_all_docs(collection_name, field_name, save_folder):
    docs = db.collection(collection_name).stream()
    for doc in docs:
        doc_data = doc.to_dict()
        if field_name in doc_data:
            image_url = doc_data[field_name]
            uid = doc_data.get('uid', 'Unknown')  # Get UID from document data, default to 'Unknown' if not found
            display_image_from_url(image_url, uid, save_folder)

def get_docs_with_status(coll_name, s_value, field_name, save_folder):
    query = db.collection(coll_name).where("Status", "==", s_value).stream()
    for doc in query:
        doc_data = doc.to_dict()
        if field_name in doc_data:
            image_url = doc_data[field_name]
            uid = doc_data.get('uid', 'Unknown')  # Get UID from document data, default to 'Unknown' if not found
            display_image_from_url(image_url, uid, save_folder)

# Example usage for "users" collection



if(db):
    field_name = 'registration_photo'
    save_folder = "image_folder"
    get_all_docs('users', field_name, save_folder)
    get_docs_with_status('users', 'some_value', field_name, save_folder)
    op.master(db)