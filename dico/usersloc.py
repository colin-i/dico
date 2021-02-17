import gi
from gi.repository import Gtk

import reqs
import users
import flist

list=users.listdef()

def show(nb):
	wn=Gtk.ScrolledWindow()
	wn.set_vexpand(True)
	sort=Gtk.TreeModelSort.new_with_model(list)
	return users.show_univ(nb,wn,sort,clkrow)

def clkrow(t,p,c,b):
	m=t.get_model()
	user=m.get_value(m.get_iter(p),0)
	flist.set(b,user)

def set():
	s=";"
	r=reqs.reque("list.local",{"separator" : s})
	list.clear()
	usrs=r.split(s)
	for x in usrs:
		list.append([x])