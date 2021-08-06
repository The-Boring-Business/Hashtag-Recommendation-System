import os

class Config:
    PROJECT_ID = os.environ.get('PROJECT_ID')
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')