"""This module defines functions to be used with the Kivy app"""
import os
import requests

#from models.ImageStore import ImageStore

def verify_image(filename):
    """Verifies whether the file exists"""
    image_extensions = ['tif', 'jpg', 'gif', 'png', 'jpeg']
    if type(filename) is str:
        extension = filename.split('.')
        if len(extension) == 2:
            if extension[1].lower() in image_extensions:
                return os.path.isfile(filename)

    return False

def convert_image(filename):
    """Converts the image and prepares it for the backend API"""
    url = 'http://0.0.0.0:5000/api/v1/image_ocr'
    print(filename)
    with open(filename, 'rb') as f:
        image = f.read()
    data = image
    headers = {'Content-Type': 'application/octet-stream'}
    r = requests.post(url, data=data, headers=headers)
    print(r.json())
    return r.json()

if __name__ == '__main__':
    print(verify_image('practice.jpeg'))
    print(verify_image('wersdfsdfasdf.txt'))
    print(verify_image('he.png'))
    print(verify_image('file.png'))
    print(verify_image('hi.JPG'))
