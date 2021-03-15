
from gi.repository import Gtk

import xml.etree.ElementTree as ET
import os.path

from . import limit
from . import nick

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
	f=Gtk.Frame(label="External data file settings")
	g=Gtk.Grid()
	lb=Gtk.Label(halign=Gtk.Align.START,label="Location")
	g.attach(lb,0,0,1,1)
	en=Gtk.Entry(buffer=file,hexpand=True)
	g.attach(en,1,0,1,1)
	lb=Gtk.Label(halign=Gtk.Align.START,label="Nick name")
	g.attach(lb,0,1,1,1)
	en=Gtk.Entry(buffer=nick.confs(),hexpand=True)
	g.attach(en,1,1,1,1)
	f.set_child(g)
	return f
def store(d):
	d['ext_file']=file.get_text()
def restore(d):
	file.set_text(d['ext_file'],-1)
