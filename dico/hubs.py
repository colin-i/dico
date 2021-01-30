
import gi
from gi.repository import Gtk,GObject

import xml.etree.ElementTree as ET
import urllib.request
import os.path

import base

addr=Gtk.EntryBuffer(text='https://www.te-home.net/?do=hublist&get=hublist.xml')
file=Gtk.EntryBuffer(text='hublist.xml')
lim=Gtk.EntryBuffer(text='200')

list=Gtk.ListStore(GObject.TYPE_STRING)

def confs():
	f=Gtk.Frame(label="Hub List")
	g=Gtk.Grid()
	lb=Gtk.Label(halign=Gtk.Align.START,label="File address")
	g.attach(lb,0,0,1,1)
	en=Gtk.Entry(buffer=addr,hexpand=True)
	g.attach(en,1,0,1,1)
	lb=Gtk.Label(halign=Gtk.Align.START,label="File fallback location")
	g.attach(lb,0,1,1,1)
	en=Gtk.Entry(buffer=file,hexpand=True)
	g.attach(en,1,1,1,1)
	lb=Gtk.Label(halign=Gtk.Align.START,label="Maximum number of entries")
	g.attach(lb,0,2,1,1)
	en=Gtk.Entry(buffer=lim,hexpand=True)
	g.attach(en,1,2,1,1)
	f.set_child(g)
	return f
def store(d):
	d['hub_file']=addr.get_text()
	d['hub_file_fallback']=file.get_text()
	d['hub_limit']=lim.get_text()
def restore(d):
	addr.set_text(d['hub_file'],-1)
	file.set_text(d['hub_file_fallback'],-1)
	lim.set_text(d['hub_limit'],-1)

def reini():
	list.clear()
	ini()

def show():
	wn=Gtk.ScrolledWindow()
	wn.set_vexpand(True)
	tree=Gtk.TreeView.new_with_model(list)
	renderer = Gtk.CellRendererText()
	column = Gtk.TreeViewColumn()
	column.set_title('Address')
	column.pack_start(renderer,True)
	column.add_attribute(renderer, "text", 0)
	tree.append_column(column)
	wn.set_child(tree)
	return wn

def ini():
	try:
		tree = ET.ElementTree(file=urllib.request.urlopen(addr.get_text()))
	except Exception:
		t=os.path.expandvars(file.get_text())
		d=os.path.dirname(t)
		if d=="":
			tree = ET.parse(base.get_root_file(t))
		else:
			tree = ET.parse(t)
	root = tree.getroot()
	hbs=root.find("Hubs").findall("Hub")
	max=int(lim.get_text())
	for i in range(max):
		list.append([hbs[i].attrib['Address']])
