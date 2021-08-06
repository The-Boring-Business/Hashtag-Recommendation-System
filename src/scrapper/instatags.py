import requests
import re
import bs4
import json

# get trending hastags from instagram
def get_trending_hashtags(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script')
        pattern = re.compile(r'window._sharedData')
        for script in scripts:
            if pattern.match(script.string):
                data = script.string.partition('=')[-1].strip(' ;')
                data = json.loads(data)
                return data['entry_data']['TagPage'][0]['tag']['top_posts']['nodes']