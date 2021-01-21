
import gi
from gi.repository import Gtk

def show(w):
	b=Gtk.Button.new_with_label(chr(0x2699))
	w.set_child(b)