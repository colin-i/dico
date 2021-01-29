
import gi
from gi.repository import Gtk

import limit
import log
import stor2
import hubs

def ini(b,win):
	d=Gtk.Dialog(title="Settings",transient_for=win)
	d.set_modal(True)
	d.add_button("_OK",Gtk.ResponseType.NONE)
	d.connect("response",verifs,win)
	if win.is_maximized():
		d.maximize()
	else:
		dim=win.get_default_size()
		d.set_default_size(dim.width,dim.height)
	bx=d.get_content_area()
	bx.set_orientation(Gtk.Orientation.VERTICAL)
	bx.append(limit.show())
	bx.append(log.show())
	bx.append(stor2.show())
	bx.append(hubs.show())
	d.show()
def verifs(d,r,w):
	limit.verifs(w)
	log.reset()
	stor2.ini()
	hubs.ini()
	d.destroy()#close is calling here twice

def entry(txt,buf):
	bx=Gtk.Box()
	lb=Gtk.Label()
	lb.set_halign(Gtk.Align.START)
	lb.set_text(txt)
	bx.append(lb)
	en=Gtk.Entry.new_with_buffer(buf)
	en.set_hexpand(True)
	bx.append(en)
	return bx
