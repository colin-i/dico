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
def restore(d):
	name.set_text(d['nick_name'],-1)

def reset():
	f=stor2.get_file()
	t = ET.parse(f)
	root = t.getroot()
	s = root.find(stor2.set).find('Nick')
	s.text=name.get_text()
	t.write(f)