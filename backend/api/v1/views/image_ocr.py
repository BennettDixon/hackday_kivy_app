#!/usr/bin/python3
"""
handles REST API actions for place
"""
from api.v1.views import app_views
from flask import jsonify
from flask import Flask
from flask import request
from flask import abort
from os import getenv

@app_views.route(
    '/image_ocr',
    methods=['POST'],
    strict_slashes=False)
def places_search():
    """processes an image and returns the text contained in it
        TODO implement
    """
    post_data = request.get_json()
    places_search = []
    if post_data is None or type(post_data) != dict:
        return jsonify({'error': 'Not a JSON'}), 400

@app_views.route('/testing', methods=['GET'], strict_slashes=False)
def testing_api():
    return '{"status": "OK" }'
