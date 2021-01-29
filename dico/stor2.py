
import gi
from gi.repository import Gtk

import xml.etree.ElementTree as ET
import os.path

import limit
import sets

file=Gtk.EntryBuffer(text='${HOME}/.config/eiskaltdc++/DCPlusPlus.xml')

def ini():
	tree = ET.parse(os.path.expandvars(file.get_text()))
	root = tree.getroot()
	limit.start=int(root.find('Settings').find('TotalUpload').text)

def show():
	return sets.entry("External data file location",file)
def store(d):
	d['ext_file']=file.get_text()
def restore(d):
	file.set_text(d['ext_file'],-1)
