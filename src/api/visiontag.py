from flask import Flask, request
from flask_restful import Resource
from PIL import Image 
import os
from google.cloud import vision
import requests
import json 
from src.model.hashtag import Prediction

         
        
class ImageApi(Resource):
    def post(self):
        image = request.files.get('image','')
        image_data = json.load(image)
        user = image_data['user']
        service = image_data['service']
        if image:
            image = Image.open(image)
        else :
            return {'Error':'No Image Found'}
        result = Prediction(image, user, service)
        return {'Response': result}

    def get(self):
        return {'Resource':'APi Running'}
