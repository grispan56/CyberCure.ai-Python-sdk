import requests
import json

def get_url_indicators(type='json',json=1):
        response = requests.get("http://api.cybercure.ai/feed/get_url", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.1' }, params={ "type": type })
        return response.text

def get_ip_indicators(type='json'):
        response = requests.get("http://api.cybercure.ai/feed/get_ips", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.1' }, params={ "type": type })
        return response.body

def get_hashindicators(type='json'):
        response = requests.get("http://api.cybercure.ai/feed/get_hash", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.1' }, params={ "type": type })
        return response.body


