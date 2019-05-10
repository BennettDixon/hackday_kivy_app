#!/usr/bin/python3
"""
Handles processing of images and sending
them to the Vision Azure API.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
import requests

@app_views.route(
    '/image_ocr',
    methods=['POST'],
    strict_slashes=False)

def process_image(img):
    """Processes an image by:
        -> saving it into a file #TODO remove this line if we decide not to go with this method
        -> sending the file to Vision Azure api
        -> returns a dictionary containing the caption
        and confidence level associated with that image
        TODO implement
    """
    # Verify Azure Vision Subscription Key
    subscription_key = vision_subscription_key
    assert subscription_key

    # Azure Vision API URL for detecting objects
    detection_url = 'https://westus.api.cognitive.microsoft.com/vision/v2.0/detect'

    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/json'}

    # POST request to Azure API to get image data
    response = requests.post(analyze_url, headers=headers, data=img_data)

    image_data = response.json()
    if image_data is None or type(image_data) is not dict:
        return jsonify({'error': 'Not a JSON'}), 400

    try:
        caption_response = CaptionResponse(image_data.get('caption'),
                                           image_data.get('confidence'))
    except (ValueError, TypeError) as error:
        abort(500) # TODO - verify this abort method, should we return a JSON error dict with a code?
    return caption_response.to_dict()



@app_views.route('/testing', methods=['GET'], strict_slashes=False)
def testing_api():
    return '{"status": "OK" }'
