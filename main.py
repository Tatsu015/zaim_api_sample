from dotenv import load_dotenv
from pyzaim import ZaimAPI
import os

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

api = ZaimAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET, 'verifier')

datas = api.get_data()
categories = api.category_itos
genres = api.genre_itos
accounts = api.account_itos

print(datas, categories, genres, accounts)
