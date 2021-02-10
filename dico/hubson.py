import gi
from gi.repository import Gtk

import hubs

list=hubs.listdef()
sort=Gtk.TreeModelSort.new_with_model(list)

def clk(b,ix):
	hubs.clk_univ(sort,ix)
def show():
	wn=Gtk.ScrolledWindow()
	wn.set_vexpand(True)
	t=hubs.treedef(sort,clk)
	wn.set_child(t)
	bx=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	bx.append(wn)
	b=Gtk.Button.new_with_label("-")
	b.connect('clicked', rem, t)
	bx.append(b)
	return bx

def rem(b,t):
	s=t.get_selection()
	d=s.get_selected()
