#!/usr/bin/python3
"""
Handles processing of images and sending
them to the Vision Azure API.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from api.v1.settings import vision_subscription_key
from api.v1.models.CaptionResponse import CaptionResponse
import json
import requests


@app_views.route(
    '/image_ocr',
    methods=['POST'],
    strict_slashes=False)
def process_image(debug=False):
    """Processes an image by:
        -> sending the file to Vision Azure api
        -> returns a dictionary containing the caption
        and confidence level associated with that image
        TODO implement
    """
    # Content-Type we are posting, testing uses json
    content_type = ''
    img = None
    if debug is True:
        content_type = 'application/json'
    else:
        content_type = 'application/octet-stream'
    img = request.data
    print(img)
    with open('/test.png', 'wb+') as myF:
        myF.write(bytes(img))
    # Verify Azure Vision Subscription Key
    subscription_key = vision_subscription_key
    # Azure Vision API URL for detecting objects
    url = 'https://westus2.api.cognitive.microsoft.com/vision/v2.0/analyze'

    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': content_type}
    # POST request to Azure API to get image data
    response = requests.post(
        url,
        headers=headers,
        params={"visualFeatures": "Description"},
        data=img
    )
    # return jsonify(json.loads(response.text))
    print(response.json())
    caption_data = response.json().get('description').get('captions')
    if caption_data is None or type(caption_data) is not list:
        return jsonify({'error': 'Not a JSON'}), 402

    try:
        caption = sorted(caption_data, key=lambda d: d.get('confidence'))[-1]
        caption_response = CaptionResponse(caption.get('text'),
                                           caption.get('confidence'))
    except (ValueError, TypeError) as error:
        msg = '{"error": "{} raised when creating CaptionResponse"}'.format(
            type(error)
        )
        return msg, 500
    return jsonify(caption_response.to_dict())


@app_views.route('/testing', methods=['GET'], strict_slashes=False)
def testing_api():
    return '{"status": "OK" }'
