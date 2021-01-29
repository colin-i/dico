
import gi
from gi.repository import Gtk

import sets

def show(w):
	bx=Gtk.Box()
	bx.set_orientation(Gtk.Orientation.VERTICAL)
	b=Gtk.Button.new_with_label(chr(0x2699))
	b.connect('clicked', sets.ini, w)
	bx.append(b)
	pags=Gtk.Notebook()
	pags.append_page(Gtk.TreeView(),Gtk.Label(label="HubList"))
	bx.append(pags)
	w.set_child(bx)