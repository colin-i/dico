import requests
import random

def req(a):
	url = "http://localhost:3121"
	payload = {
		"id" : random.randint(0,(2**16)-1),
		"jsonrpc" : "2.0",
		"method" : a,
		"version" : "2.0"
	}
	response = requests.post(url, json=payload).json()
	return response['result']