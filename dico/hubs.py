
import gi
from gi.repository import Gtk

import xml.etree.ElementTree as ET
import urllib.request
import os.path

import base
import hubscon

addr=Gtk.EntryBuffer(text='https://www.te-home.net/?do=hublist&get=hublist.xml')
file=Gtk.EntryBuffer(text='hublist.xml')
lim=Gtk.EntryBuffer(text='200')

list=Gtk.ListStore(str,int,str)
sort=Gtk.TreeModelSort.new_with_model(list)

from enum import IntEnum
class COLUMNS(IntEnum):
	ADDRESS=0
	USERS=1
	COUNTRY=2

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

def clk(b,ix):
	n=sort.get_sort_column_id()
	if n[1]!=Gtk.SortType.ASCENDING:
		sort.set_sort_column_id(ix,Gtk.SortType.ASCENDING)
	else:
		sort.set_sort_column_id(ix,Gtk.SortType.DESCENDING)
def col(tr,tx,ix):
	renderer = Gtk.CellRendererText()
	column = Gtk.TreeViewColumn()
	column.set_title(tx)
	column.pack_start(renderer,True)
	column.add_attribute(renderer, "text", ix)
	b=column.get_button()
	b.connect('clicked', clk, ix)
	tr.append_column(column)
def show():
	wn=Gtk.ScrolledWindow()
	wn.set_vexpand(True)
	tree=Gtk.TreeView.new_with_model(sort)
	col(tree,'Address',COLUMNS.ADDRESS)
	col(tree,'Users',COLUMNS.USERS)
	col(tree,'Country',COLUMNS.COUNTRY)
	tree.connect("row-activated",hubscon.add,sort)
	tree.set_activate_on_single_click(True)
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
	mx=min(int(lim.get_text()),len(hbs))
	for i in range(mx):
		attrs=hbs[i].attrib
		list.append([attrs['Address'],int(attrs['Users']),attrs['Country']])
