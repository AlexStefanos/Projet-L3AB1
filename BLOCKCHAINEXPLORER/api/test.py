import json
from urllib import request
import requests

url = 'http://127.0.0.1:8000/api/get/'

json_data = requests.get(url).json()

print(json_data)