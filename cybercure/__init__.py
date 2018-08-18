import requests

def get_url_indicators(typ='json',json=1):
	response = requests.get("http://api.cybercure.ai/feed/get_url", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.2' }, params={ "type": typ })
	return response.text

def get_ip_indicators(type='json',return_type='json'):
	response = requests.get("http://api.cybercure.ai/feed/get_ips", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.2' }, params={ "type": type })
	if type == 'json' or type == 'stix' and return_type == 'json':
		return response.json()
	else:
		return response.text

def get_hash_indicators(type='json',json=1):
        	response = requests.get("http://api.cybercure.ai/feed/get_hash", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.2' }, params={ "type": type })
        	return response.text

def search(indicator):
                response = requests.get("http://api.cybercure.ai/feed/search", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.2' }, params={ "value": indicator })
                return response.json()
