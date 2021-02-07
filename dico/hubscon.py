
import gi
from gi.repository import GLib

import time

import hubs
import reqs

cons=[]
recons=[]
def con(a):
	for x in recons:
		if x==a:
			return
	acon(a)
def acon(a):
	try:
		reqs.requ("hub.add",{"enc" : "", "huburl" : a})
	except Exception:
		recons.append(a)
		GLib.timeout_add_seconds(5,bcon,a)
def bcon(a):
	recons.remove(a)
	acon(a)
	return False

def add(tree,path,column,model):
	it=model.get_iter(path)
	adr=model.get_value(it,hubs.COLUMNS.ADDRESS)
	con(adr)
	cons.append(adr)

def recon():
	for x in cons:
		con(x)
