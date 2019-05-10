#!/usr/bin/python3
"""Image store class for storing image data
"""
from models.BaseModel import BaseModel

# Create your models here.
class ImageStore(BaseModel):
    """ Image class for representing objects received in posts
    """
    width = 0
    height = 0
    byte_arr = 0
    def __init__(self, width, height, byte_arr):
        self.width = width
        self.height = height
        self.byte_array = byte_arr
        super().__init__()

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if (value is None or not isinstance(value, int)):
            raise TypeError("width of Image must be int")
        elif (value < 0):
            raise ValueError("width of Image must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if (value is None or not isinstance(value, int)):
            raise TypeError("height of Image must be int")
        elif (value < 0):
            raise ValueError("height of Image must be >= 0")

        self.__height = value

    @property
    def byte_array(self):
        """getter for image data, byte_array should be base_64 encoded"""
        return self.__byte_array

    @byte_array.setter
    def byte_array(self, value):
        """setter for image data, TODO base64 encode"""
        if (value is None):
            raise TypeError("width of Image must be not None")

        self.__byte_array = value
