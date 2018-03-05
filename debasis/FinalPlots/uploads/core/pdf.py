import cv2
import os

my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
spath = os.path.join(my_path, 'static/images/figure0.png')

def load_images_from_folder(spath):
    images = []
    for filename in os.listdir(spath):
        img = cv2.imread(os.path.join(spath,filename))
        if img is not None:
            images.append(img)
    return images


