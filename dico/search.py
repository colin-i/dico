import gi
from gi.repository import Gtk

def show():
	wn=Gtk.ScrolledWindow()
	wn.set_vexpand(True)
	return wn
