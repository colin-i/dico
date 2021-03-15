
class detail():
	def __init__(self,a,b,c):
		self.nick=a
		self.hub=b
		self.fslots=c

def create(r,free):
	return detail(r["Nick"],r["Hub URL"],free)

def update(r,free,lst,it,col):
	ar=lst.get_value(it,col)
	ar.append(create(r,free))
	lst.set_value(it,col,ar)

from gi.repository import Gtk

from . import users
from . import hubs

from enum import IntEnum
class COLUMNS(IntEnum):
	NICK=0
	HUB=1
	FSLOTS=2

list=Gtk.ListStore(str,str,str)
sort=Gtk.TreeModelSort.new_with_model(list)

def show():
	scroll=Gtk.ScrolledWindow()
	scroll.set_vexpand(True)
	tree=Gtk.TreeView.new_with_model(sort)
	hubs.col(tree,'Nick',COLUMNS.NICK,clk)
	hubs.col(tree,'Hub URL',COLUMNS.HUB,clk)
	hubs.col(tree,'Free Slots',COLUMNS.FSLOTS,clk)
	tree.connect("row-activated",clkrow,sort)
	tree.set_activate_on_single_click(True)
	scroll.set_child(tree)
	return scroll
def clk(b,ix):
	hubs.clk_univ(sort,ix)
def clkrow(tree,path,column,model):
	it=model.get_iter(path)
	users.ldload(model.get_value(it,COLUMNS.HUB),model.get_value(it,COLUMNS.NICK))

def set(ar):
	list.clear()
	for x in ar:
		list.append([x.nick,x.hub,x.fslots])