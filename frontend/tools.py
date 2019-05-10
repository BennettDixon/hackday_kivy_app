"""This module defines functions to be used with the Kivy app"""
import os
from PIL import Image

def verify_image(filename):
    """Verifies whether the file exists"""
    image_extensions = ['tif', 'jpg', 'gif', 'png', 'jpeg']
    if type(filename) is str:
        extension = filename.split('.')
        if len(extension) == 2:
            if extension[1] in image_extensions:
                return True

    return False

def convert_image(filename):
    """Converts the image and prepares it for the backend API"""
    with Image.open(filename) as image: 
        pass

if __name__ == '__main__':
    print(verify_image('practice.jpeg'))
    print(verify_image('wersdfsdfasdf.txt'))
    print(verify_image('he.png'))
