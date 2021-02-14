import gi
from gi.repository import Gtk

import hubs
import reqs

list=Gtk.ListStore(str)
sort=Gtk.TreeModelSort.new_with_model(list)
scroll=Gtk.ScrolledWindow()

def show(nb):
	scroll.set_vexpand(True)
	t=Gtk.TreeView.new_with_model(sort)
	renderer = Gtk.CellRendererText()
	column = Gtk.TreeViewColumn()
	column.set_title("Name")
	column.pack_start(renderer,True)
	column.add_attribute(renderer, "text", 0)
	b=column.get_button()
	b.connect('clicked', clk, None)
	t.append_column(column)
	t.connect("row-activated",clkrow,nb)
	t.set_activate_on_single_click(True)
	scroll.set_child(t)
	return scroll
def clk(b,d):
	hubs.clk_univ(sort,0)
def clkrow(t,p,c,b):
	m=t.get_model()
	user=m.get_value(m.get_iter(p),0)
	adr=b.get_tab_label_text(scroll)
	reqs.requ("list.download",{"huburl" : adr, "nick" : user})

def set(nb,adr,lst):
	list.clear()
	nb.set_tab_label_text(scroll,adr)
	for x in lst:
		list.append([x])