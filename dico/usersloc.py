import gi
from gi.repository import Gtk

import reqs

def show():
	wn=Gtk.ScrolledWindow()
	wn.set_vexpand(True)
	return wn

def set():
	r=reqs.reque("list.local",{"separator" : ";"})
