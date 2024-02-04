import base_model as bm
import os
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
import connlogin as cn
# import firebase_admin
# from firebase_admin import credentials, firestore

cn.master()

def image_parse_dir():
    image_files_path = []
    image_directory = 'new_image_folder'
    image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for i in image_files:
        image_files_path.append(image_directory+'/'+i)
    return image_files_path

def array_parse_dir():
    file_path = []
    directory = 'new_image_folder'
    files = [f for f in os.listdir(directory) if f.lower().endswith(('_array.txt'))]
    # print(files)
    file_path.append(directory+'/'+files[0])
    file = open(file_path[0], 'r')
    text = file.read()
    file.close()
    list_array = text.split('\n')
    # list_array
    list_array.remove('')
    array = np.asarray(list_array)
    return array

file_path = []
def parse_dir():
    directory = 'new_image_folder'
    files = [f for f in os.listdir(directory) if f.lower().endswith(('.txt'))]
    file_path.append(directory+'/'+files[0])
    return file_path

files = parse_dir()
file = open(files[0], 'r')
uid = file.read()
file.close()

def master_li():
    image_files_path = image_parse_dir()
    array = array_parse_dir()
    # print(array.dtype)
    array = np.float64(array)
    # print(array.dtype)
    image = mpimg.imread(image_files_path[0])
    # bm.error_detection(image)
    encoding = bm.face_embed(image)
    # print(encoding[0].dtype)
    if bm.face_recognition.compare_faces([array], encoding[0]):
        return 'yes'
    return 'no'

stat = master_li()

# cred1 = credentials.Certificate("C:/Users/swast/Downloads/snapverify-e7124-firebase-adminsdk-wvdy8-c27bd424f8.json")
# firebase_admin.initialize_app(cred1)
# db = firestore.client()

def update_login_request_status(user_id, new_status):
    doc_ref = cn.db.collection('users').document(user_id)
    doc_ref.update({'login_request': new_status})
    print(f"Login request status updated to {new_status} for user {user_id}.")

def main():
    user_id = uid
    login_request_input = stat
    if login_request_input == 'yes':
        update_login_request_status(user_id, True)
    elif login_request_input == 'no':
        print("Login request status remains unchanged.")
    else:
        print("Invalid input. Login request status remains unchanged.")

if __name__ == "__main__":
    main()