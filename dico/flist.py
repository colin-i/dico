import gi
from gi.repository import Gtk

name=Gtk.Label()
bx=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

def show():
	scroll=Gtk.ScrolledWindow()
	scroll.set_vexpand(True)
	bx.append(name)
	bx.append(scroll)
	return bx

def set(nb,nm):
	name.set_text(nm)
	z=nm.split(".")
	nb.set_tab_label_text(bx,z[0])