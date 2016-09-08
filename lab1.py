#encoding: UTF-8

import requests

response = requests.get("https://github.com/annypanny/CMPUT404lab1/raw/master/lab1.py")

print response.text
