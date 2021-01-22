
import gi
from gi.repository import Gtk

import sets

def show(w):
	b=Gtk.Button.new_with_label(chr(0x2699))
	b.connect('clicked', sets.ini, w)
	w.set_child(b)