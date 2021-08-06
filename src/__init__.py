from flask import Flask
from flask_restful import Api
from src.routes.routes import initialize_routes
import os
from flask_cors import CORS

# Place where app is defined
app = Flask(__name__)

Api = Api(app)
CORS(app, resources={r'/*':{"origins": "*"}},allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Methods"])
#CORS(app)

initialize_routes(Api)
