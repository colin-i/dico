
import gi
from gi.repository import Gtk

file=Gtk.EntryBuffer(text='')

def sets():
	bx=Gtk.Box()
	lb=Gtk.Label()
	lb.set_halign(Gtk.Align.START)
	lb.set_text("Hub list address")
	bx.append(lb)
	en=Gtk.Entry.new_with_buffer(file)
	en.set_hexpand(True)
	bx.append(en)
	return bx
