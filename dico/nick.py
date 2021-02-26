import gi
from gi.repository import Gtk

import xml.etree.ElementTree as ET

import stor2
import main
import daem

name=Gtk.EntryBuffer(text='dico')

def confs():
	return name
def store(d):
	d['nick_name']=name.get_text()
def restore(d):
	name.set_text(d['nick_name'],-1)
def ini(restart):
	f=stor2.get_file()
	t = ET.parse(f)
	root = t.getroot()
	se = root.find(stor2.set)
	r=see(se,'Nick','string',name)
	#Slots not working r|=see(se,'Slots','int',slots)
	if r==1:
		if restart:
			main.dclose()
		t.write(f)
		if restart:
			daem.restart()

def see(se,n,t,b):
	txt=b.get_text()
	s = se.find(n)
	if s==None:
		s=ET.SubElement(se,n)
		s.set('type',t)
		s.text=txt
		return 1
	elif txt!=s.text:
		s.text=txt
		return 1
	return 0
