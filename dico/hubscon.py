
import gi
from gi.repository import GLib

import time

import hubs
import reqs
import hubson

cons=[]
recons=[]
class reconnect():
	def __init__(self,adr):
		self.adr=adr

def acon(a):
	try:
		reqs.requ("hub.add",{"enc" : "", "huburl" : a})
	except Exception:
		r=reconnect(a)
		r.id=GLib.timeout_add_seconds(3,bcon,r)
		recons.append(r)
def bcon(r):
	acon(r.adr)
	recons.remove(r)
	return False

def add(tree,path,column,model):
	it=model.get_iter(path)#iter free is in the bindings
	d=[]
	for i in hubs.COLUMNS:
		d.append(model.get_value(it,i))
	addcon(model,d)
def addcon(model,rowlst):
	adr=rowlst[hubs.COLUMNS.ADDRESS]
	for x in cons:
		if x==adr:
			return
	cons.append(adr)
	acon(adr)
	hubson.add(rowlst)
def remcon(a):
	cons.remove(a)
	reqs.requ("hub.del",{"huburl" : a})
	hclose(a)

def recon():
	for x in cons:
		for a in recons:
			if x==a.adr:
				return
		acon(x)

def close():
	for x in recons:
		GLib.source_remove(x.id)
def hclose(a):
	for x in recons:
		if x.adr==a:
			GLib.source_remove(x.id)
			return
