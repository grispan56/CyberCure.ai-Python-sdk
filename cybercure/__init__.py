import requests

class CyberCure:

	#def __init__(self):
		
	def get_url_indicators(typ='json',json=1):
        	response = requests.get("http://api.cybercure.ai/feed/get_url", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.1' }, params={ "type": typ })
        	return response.text

	def get_ip_indicators(self,type='json'):
        	response = requests.get("http://api.cybercure.ai/feed/get_ips", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.1' }, params={ "type": type })
		if type == 'json' or type == 'stix':
        		return response.json()
		else:
			return response.text
	def get_hashindicators(self,type='json',json=1):
        	response = requests.get("http://api.cybercure.ai/feed/get_hash", headers={ "Accept": "application/json",'user-agent': 'cybercure-python-sdk/0.0.1' }, params={ "type": type })
        	return response.text


