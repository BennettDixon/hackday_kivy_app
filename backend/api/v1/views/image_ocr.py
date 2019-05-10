#!/usr/bin/python3
"""
Handles processing of images and sending
them to the Vision Azure API.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from api.v1.settings import vision_subscription_key
import json
import requests


@app_views.route(
    '/image_ocr',
    methods=['POST'],
    strict_slashes=False)
def process_image(debug=True):
    """Processes an image by:
        -> sending the file to Vision Azure api
        -> returns a dictionary containing the caption
        and confidence level associated with that image
        TODO implement
    """
    # Content-Type we are posting, testing uses json
    content_type = ''
    if debug is True:
        content_type = 'application/json'
    else:
        content_type = 'application/octet-stream'
    img = request.get_json()
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
        json={"url": img.get('url')}
    )
    # return jsonify(json.loads(response.text))

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
    return caption_response.to_dict()


@app_views.route('/testing', methods=['GET'], strict_slashes=False)
def testing_api():
    return '{"status": "OK" }'
