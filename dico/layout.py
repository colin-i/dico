
import gi
from gi.repository import Gtk

import sets
import hubs
import hubson
import users
import usersloc
import flist
import search
 
def show(w):
	bx=Gtk.Box()
	bx.set_orientation(Gtk.Orientation.VERTICAL)
	b=Gtk.Button.new_with_label(chr(0x2699))
	b.connect('clicked', sets.ini, w)
	bx.append(b)
	pags=Gtk.Notebook()
	pags.append_page(hubs.show(),Gtk.Label(label="HubList"))
	pags.append_page(hubson.show(pags),Gtk.Label(label="Hubs"))
	pags.append_page(users.show(pags),Gtk.Label(label=users.intro))
	locale=usersloc.show(pags)
	pags.append_page(locale,Gtk.Label(label="Users"))
	pags.append_page(flist.show(),Gtk.Label(label="FileList"))
	pags.append_page(search.show(),Gtk.Label(label="Search"))
	pags.connect("switch-page",sw,locale)
	bx.append(pags)
	w.set_child(bx)

def sw(notebook,page,page_num,data):
	if page==data:
		usersloc.set()