import requests
import random

url = "http://localhost:3121"
jsonrpcversion="2.0"
def req(a):
	payload = {
		"id" : random.randint(0,(2**16)-1),
		"jsonrpc" : jsonrpcversion,
		"method" : a,
		"version" : jsonrpcversion
	}
	response = requests.post(url, json=payload).json()
	return response['result']
def requ(a,para):
	payload = {
		"id" : random.randint(0,(2**16)-1),
		"jsonrpc" : jsonrpcversion,
		"method" : a,
		"version" : jsonrpcversion,
		"params" : para
	}
	requests.post(url, json=payload).json()