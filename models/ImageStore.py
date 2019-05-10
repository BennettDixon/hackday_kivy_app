#!/usr/bin/python3
"""Image store class for storing image data
"""
from models.base_model import BaseModel

# Create your models here.
class ImageStore(BaseModel):
    """ Image class for representing objects received in posts
    """
    def __init__(self, width, height, byte_arr):
        self.width = width
        self.height = height
        self.byte_array = byte_arr

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (value is None or not isinstance(value, int)):
            raise TypeError("width of Image must be int")
        elif (value < 0):
            raise ValueError("width of Image must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (value is None or not isinstance(value, int)):
            raise TypeError("height of Image must be int")
        elif (value < 0):
            raise ValueError("height of Image must be >= 0")

        self.__height = value

    @property
    def byte_array(self):
        return self.__byte_array

    @byte_array.setter
    def byte_array(self, value):
        if (value is None):
            raise TypeError("width of Image must be not None")

        self.__byte_array = value
