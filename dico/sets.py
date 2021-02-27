
import gi
from gi.repository import Gtk

from . import limit
from . import log
from . import stor2
from . import nick
from . import hubs
from . import daem
from . import search
from . import dload

def ini(b,win):
	d=Gtk.Dialog(title="Settings",transient_for=win)
	d.set_modal(True)
	d.add_button("_OK",Gtk.ResponseType.NONE)
	d.connect("response",reset,win)
	if win.is_maximized():
		d.maximize()
	else:
		dim=win.get_default_size()
		d.set_default_size(dim.width,dim.height)
	bx=d.get_content_area()
	bx.set_orientation(Gtk.Orientation.VERTICAL)
	bx.append(limit.confs())
	bx.append(log.confs())
	bx.append(stor2.confs())
	bx.append(hubs.confs())
	bx.append(daem.confs())
	bx.append(search.confs())
	bx.append(dload.confs())
	d.show()
def reset(d,r,w):
	limit.reset(w)
	log.reset()
	stor2.ini()
	dload.reset()#when daemon running
	wasreset=nick.ini(True)
	hubs.reset()
	if not wasreset:
		daem.reset()
	search.reset()
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
