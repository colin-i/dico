import gi
from gi.repository import Gtk

import hubs

list=hubs.listdef()

def show():
	wn=Gtk.ScrolledWindow()
	wn.set_vexpand(True)
	wn.set_child(hubs.treedef(list))
	return wn
