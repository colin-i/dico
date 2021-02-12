import gi
from gi.repository import Gtk

import hubs
import hubscon

list=hubs.listdef()
sort=Gtk.TreeModelSort.new_with_model(list)

def clk(b,ix):
	hubs.clk_univ(sort,ix)
def show():
	wn=Gtk.ScrolledWindow()
	wn.set_vexpand(True)
	t=hubs.treedef(sort,clk,rowclk)
	wn.set_child(t)
	bx=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	bx.append(wn)
	b=Gtk.Button.new_with_label("-")
	b.connect('clicked', rem, t)
	bx.append(b)
	return bx

def rem(b,t):
	s=t.get_selection()
	d=s.get_selected()#iter free is in the bindings
	adr=d[0].get_value(d[1],hubs.COLUMNS.ADDRESS)
	hubscon.hclose(adr)
	list.remove(d[0].convert_iter_to_child_iter(d[1]))

def rowclk(tree,path,column,model):
	pass