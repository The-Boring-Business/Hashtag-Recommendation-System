import os

class Config:
    PROJECT_ID = os.environ.get('PROJECT_ID')
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
    TWITTER_SECRET = os.environ.get('TWITTER_SECRET')