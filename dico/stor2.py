
import gi
from gi.repository import Gtk

import xml.etree.ElementTree as ET
import os.path

import limit

file=Gtk.EntryBuffer(text='${HOME}/.config/eiskaltdc++/DCPlusPlus.xml')

def ini():
	tree = ET.parse(os.path.expandvars(file.get_text()))
	root = tree.getroot()
	limit.start=int(root.find('Settings').find('TotalUpload').text)

def sets():
	bx=Gtk.Box()
	lb=Gtk.Label()
	lb.set_halign(Gtk.Align.START)
	lb.set_text("External data file location")
	bx.append(lb)
	en=Gtk.Entry.new_with_buffer(file)
	en.set_hexpand(True)
	bx.append(en)
	return bx
def store(d):
	d['ext_file']=file.get_text()
def restore(d):
	file.set_text(d['ext_file'],-1)
