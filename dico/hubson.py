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

def add(a):
	list.append(a)
def rem(b,t):
	s=t.get_selection()
	d=s.get_selected()#iter free is in the bindings
	hubscon.remcon(d[0].get_value(d[1],hubs.COLUMNS.ADDRESS))
	list.remove(d[0].convert_iter_to_child_iter(d[1]))

def rowclk(tree,path,column,model):
	pass

def store(d):
	l=[]
	for r in list:
		v=[]
		for i in hubs.COLUMNS:
			v.append(list.get_value(r.iter,i))
		l.append(v)
	d['hubs']=l
def restore(d):
	l=d['hubs']
	for r in l:
		hubscon.addcon(list,r)