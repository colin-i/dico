import gi
from gi.repository import Gtk

import reqs
import flist

def show():
	scroll=Gtk.ScrolledWindow()
	scroll.set_vexpand(True)
	return scroll

def add(m,it):
	xt=m.get_value(it,flist.COLUMNS.TTH)
	xl=m.get_value(it,flist.COLUMNS.SIZE)
	dn=m.get_value(it,flist.COLUMNS.NAME)
	m="magnet:?xt=urn:tree:tiger:"+xt+"&xl="+str(xl)+"&dn="+dn
	reqs.requ("magnet.add",{"directory" : "","magnet" : m})
