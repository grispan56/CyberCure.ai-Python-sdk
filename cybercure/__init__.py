import requests

useragent = 'cybercure-python-sdk/0.4.5'

def get_url_indicators(typ='json',json=1):
	""" Get URL indicators of compromise to use."""
	response = requests.get("https://api.cybercure.ai/feed/get_url", headers={ "Accept": "application/json",'user-agent': useragent }, params={ "type": typ })
	return response.text

def get_ip_indicators(type='json',return_type='json'):
	""" Get IP indicators of compromise to use"""
	response = requests.get("https://api.cybercure.ai/feed/get_ips", headers={ "Accept": "application/json",'user-agent': useragent }, params={ "type": type })
	if type == 'json' or type == 'stix' and return_type == 'json':
		return response.json()
	else:
		return response.text

def get_hash_indicators(type='json',json=1):
	""" Get Hash indicators of compromise"""
	response = requests.get("https://api.cybercure.ai/feed/get_hash", headers={ "Accept": "application/json",'user-agent': useragent }, params={ "type": type })
	return response.text

def search(indicator):
	""" Perform search for indicators. """
	response = requests.get("https://api.cybercure.ai/feed/search", headers={ "Accept": "application/json",'user-agent': useragent }, params={ "value": indicator })
	return response.json()
