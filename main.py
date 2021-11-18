import json
import requests
from requests.api import request

url = 'API URL HERE' #just replace the text with your desired API URL

def blablabla(): #replace the blablabla with whatever you'd like to call it
    response = requests.get(url)
    data = json.loads(response.text)
    return str(data)
print (blablabla())