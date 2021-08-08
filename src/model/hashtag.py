import re
import bs4
import requests
import json
from google.cloud import vision

class Prediction:
    insta_base_url = 'https://www.instagram.com/explore/tags/'
    twitter_base_url = 'https://api.twitter.com/1.1/'
    def __init__(self, image, user, services):
        self.image = image
        self.user = user
        self.services = services
        self.labels = []

    def prediction_handler(self):
        #generate hastags based on User niche
        # get user neiche from api
        #self.labels = self.vison_prediction()
        #niche = requests.get('/user/'+user+'/niche')
        niche = "travel"
        # use Jina.ai to get hashtags based on user neiche
        return self.niche_prediction(niche)
    
    @staticmethod
    def extract_shared_data(doc):
        for script_tag in doc.find_all("script"):
            if script_tag.text.startswith("window._sharedData ="):
                shared_data = re.sub("^window\._sharedData = ", "", script_tag.text)
                shared_data = re.sub(";$", "", shared_data)
                shared_data = json.loads(shared_data)
                return shared_data
    def get_twitter_trending_tags(self, tag):
        '''
        get tweets based on hashtags
        '''
        


    def niche_prediction(self, niche):
            '''
            Using Jina to get hashtags based on user niche
            '''
            services = self.services
            if 'twitter' in services:
                # get hashtags from twitter
                pass
            if 'instagram' in services:
                url = self.insta_base_url + niche
                response = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
                shared_data = self.extract_shared_data(response)
                media=shared_data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']
                captions = []
            for post in media:
                if post['node']['edge_media_to_caption']['edges'] != []:
                    self.labels.append(post['node']['edge_media_to_caption']['edges'][0]['node']['text'])
            return self.labels
'''
    def vison_prediction(self):
        # Google vision based hashtag gen
        client = vision.ImageAnnotatorClient()    
        response = client.label_detection(image=self.image)
        labels = []
        for label in response.label_annotations:
            if label.score > 0.7:
                labels.append(label.description)
        return labels'''
    
def return_all_hashtags(tweets, tag):
    all_hashtags = []
    for tweet in tweets:
        for word in tweet.split():
            if word.startswith('#') and word.lower() != '#' + tag.lower():
                all_hashtags.append(word.lower())
    return all_hashtags
