import gi
from gi.repository import Gtk

import xml.etree.ElementTree as ET

import sets
import stor2
import main
import daem

name=Gtk.EntryBuffer(text='dico')

def confs():
	return sets.entry("Nick Name",name)
def store(d):
	d['nick_name']=name.get_text()
def restore(d):
	name.set_text(d['nick_name'],-1)
def ini(restart):
	f=stor2.get_file()
	t = ET.parse(f)
	root = t.getroot()
	se = root.find(stor2.set)
	nk='Nick'
	s = se.find(nk)
	a=s==None
	if a:
		s=ET.SubElement(se,nk)
		s.set('type','string')
	else:
		a=name.get_text()!=s.text
	if a:
		if restart:
			main.dclose()
		s.text=name.get_text()
		t.write(f)
		if restart:
			daem.restart()
