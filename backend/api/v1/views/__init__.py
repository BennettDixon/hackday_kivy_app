#!/usr/bin/python3
"""init file for views in REST API
"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.image_ocr import *
