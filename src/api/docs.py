from flask import Flask, request
from flask_restful import Resource


class Home(Resource):
    def get(self): 
        return "API is running"