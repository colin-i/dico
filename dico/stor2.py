
import gi
from gi.repository import Gtk

import xml.etree.ElementTree as ET
import os.path

import limit
import sets

file=Gtk.EntryBuffer(text='${HOME}/.config/eiskaltdc++/DCPlusPlus.xml')
set='Settings'

def get_file():
	return os.path.expandvars(file.get_text())

def ini():
	f = get_file()
	t = ET.parse(f)
	root = t.getroot()
	s = root.find(set)
	limit.start=int(s.find('TotalUpload').text)
def confs():
	return sets.entry("External data file location",file)
def store(d):
	d['ext_file']=file.get_text()
def restore(d):
	file.set_text(d['ext_file'],-1)
