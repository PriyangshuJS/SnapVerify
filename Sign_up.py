import base_model as bm
import os
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

image_files_path = []
def parse_dir():
    image_directory = 'image_folder'
    image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for i in image_files:
        image_files_path.append(image_directory+'/'+i)

def master():
    parse_dir()
    image = mpimg.imread(image_files_path[0])
    # bm.error_detection(image)
    encoding = bm.face_embed(image)
    print(encoding[0])
    return encoding[0]
