import firebase_admin
from firebase_admin import credentials, firestore
from PIL import Image
import requests
from io import BytesIO
import os
from urllib.parse import urlparse

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

def get_all_docs(db, collection_name, field_name, save_folder):
    docs = db.collection(collection_name).stream()
    for doc in docs:
        doc_data = doc.to_dict()
        if field_name in doc_data:
            data = doc_data[field_name]
            if isinstance(data, list):  # Check if data is an array
                # Write array data to a .txt file
                uid = doc_data.get('uid', 'Unknown')  # Get UID from document data, default to 'Unknown' if not found
                array_file_path = os.path.join(save_folder, f"{uid}_array.txt")
                with open(array_file_path, 'w') as array_file:
                    for item in data:
                        array_file.write(str(item) + '\n')
                    print(f"Array data saved to: {array_file_path}")
            else:
                image_url = data
                uid = doc_data.get('uid', 'Unknown')  # Get UID from document data, default to 'Unknown' if not found
                display_image_from_url(image_url, uid, save_folder)

def get_docs_with_status(db, coll_name, s_value, field_name, save_folder):
    query = db.collection(coll_name).where("Status", "==", s_value).stream()
    for doc in query:
        doc_data = doc.to_dict()
        if field_name in doc_data:
            data = doc_data[field_name]
            if isinstance(data, list):  # Check if data is an array
                # Write array data to a .txt file
                uid = doc_data.get('uid', 'Unknown')  # Get UID from document data, default to 'Unknown' if not found
                array_file_path = os.path.join(save_folder, f"{uid}_array.txt")
                with open(array_file_path, 'w') as array_file:
                    for item in data:
                        array_file.write(str(item) + '\n')
                    print(f"Array data saved to: {array_file_path}")
            else:
                image_url = data
                uid = doc_data.get('uid', 'Unknown')  # Get UID from document data, default to 'Unknown' if not found
                display_image_from_url(image_url, uid, save_folder)

# Example usage for "users" collection
def master():
    
    field_name = 'login_photo'
    fielddname = 'array'
    save_folder = "new_image_folder"
    get_all_docs(db, 'users', field_name, save_folder)
    get_all_docs(db, 'users', fielddname, save_folder)
    get_docs_with_status(db, 'users', 'some_value', field_name, save_folder)
    get_docs_with_status(db, 'users', 'some_value', fielddname, save_folder)
