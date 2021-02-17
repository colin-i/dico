import gi
from gi.repository import Gtk

scroll=Gtk.ScrolledWindow()

def show():
	scroll.set_vexpand(True)
	return scroll

def set(b,nm):
	b.set_tab_label_text(scroll,nm)
