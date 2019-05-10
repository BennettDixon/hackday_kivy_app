#!/usr/bin/python3
"""Image store class for storing image data
"""
from models.BaseModel import BaseModel

# Create your models here.
class CaptionResponse(BaseModel):
    """ CaptionResponse class for responding to image post requests to
        our api
    """
    def __init__(self, caption, confidence):
        """custom init method for CaptionResponse"""
        self.caption = caption
        self.confidence = confidence

    @property
    def caption(self):
        """getter for caption private property"""
        return self.__caption

    @caption.setter
    def caption(self, value):
        """setter for caption private property"""
        if (value is None or not isinstance(value, str)):
            raise TypeError("caption of response must be str")
        elif (len(value) <= 0):
            raise ValueError("caption of response len must be > 0")
        self.__caption = value

    @property
    def confidence(self):
        """Getter for confidence attribute"""
        return self.__confidence

    @confidence.setter
    def confidence(self, value):
        """setter for confidence attribute"""
        if (value is None or not isinstance(value, float)):
            raise TypeError("confidence of caption response must be float")
        elif (value <= 0):
            raise ValueError("confidence of caption response must be > 0")
        self.__confidence = value
