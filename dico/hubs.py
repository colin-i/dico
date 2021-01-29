
import gi
from gi.repository import Gtk

import xml.etree.ElementTree as ET
import urllib.request
import os.path

import sets

addr=Gtk.EntryBuffer(text='https://www.te-home.net/?do=hublist&get=hublist.xml')
file=Gtk.EntryBuffer(text='hublist.xml')

def show():
	bx=Gtk.Box()
	bx.set_orientation(Gtk.Orientation.VERTICAL)
	bx.append(sets.entry("Hub list address",addr))
	bx.append(sets.entry("Hub fallback list file",file))
	return bx
def store(d):
	d['hub_file']=addr.get_text()
	d['hub_fallback_file']=file.get_text()
def restore(d):
	addr.set_text(d['hub_file'],-1)
	file.set_text(d['hub_fallback_file'],-1)

def ini():
	try:
		tree = ET.ElementTree(file=urllib.request.urlopen(addr.get_text()))
	except Exception:
		t=file.get_text()
		d=os.path.dirname(t)
		if d=="":
			f=base.get_root_file(t)
		else:
			f=os.path.expandvars(t)
		tree = ET.parse(f)
	root = tree.getroot()
