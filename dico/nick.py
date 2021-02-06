import gi
from gi.repository import Gtk

import xml.etree.ElementTree as ET

import sets
import stor2

name=Gtk.EntryBuffer(text='')

def confs():
	return sets.entry("Nick Name",name)
def store(d):
	d['nick_name']=name.get_text()
	f=stor2.get_file()
	t = ET.parse(f)
	root = t.getroot()
	se = root.find(stor2.set)
	nk='Nick'
	s = se.find(nk)
	if s==None:
		s=ET.SubElement(se,nk)
		s.set('type','string')
	s.text=d['nick_name']
	t.write(f)
def restore(d):
	name.set_text(d['nick_name'],-1)
