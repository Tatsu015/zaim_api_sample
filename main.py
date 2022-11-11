from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import os, sys
import json

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = OAuth1Session(
            client_key=CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=ACCESS_TOKEN,
            resource_owner_secret=ACCESS_SECRET,
            callback_uri="https://www.zaim.net/",
            verifier='verifier',
        )
url = 'https://api.zaim.net/v2/home/money/payment'
params = {
    'mapping': 1,
    'category_id': '1',
    'genre_id': '1',
    'amount': '100',
    'date': '2022-11-11',
}
data = auth.post(url, params)
print(json.dumps(data.json()))
