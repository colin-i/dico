import gi
from gi.repository import Gtk

import reqs
import hubs

from enum import IntEnum
class COLUMNS(IntEnum):
	NAME=0
	TTH=1

name=Gtk.Label()
folder=Gtk.Label()
bx=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
list=Gtk.ListStore(str,str)
sort=Gtk.TreeModelSort.new_with_model(list)
sep="\\"

def show():
	scroll=Gtk.ScrolledWindow()
	scroll.set_vexpand(True)
	tree=Gtk.TreeView.new_with_model(sort)
	hubs.col(tree,'Name',COLUMNS.NAME,clk)
	hubs.col(tree,'TTH',COLUMNS.TTH,clk)
	tree.connect("row-activated",clkrow,sort)
	tree.set_activate_on_single_click(True)
	scroll.set_child(tree)
	bx.append(name)
	bx.append(folder)
	back=Gtk.Button.new_with_label('..')
	back.connect('clicked',backing,None)
	bx.append(back)
	bx.append(scroll)
	return bx
def clk(b,ix):
	hubs.clk_univ(sort,ix)
def clkrow(tree,path,column,model):
	it=model.get_iter(path)
	if not model.get_value(it,COLUMNS.TTH):
		fshow(name.get_text(),folder.get_text()+model.get_value(it,COLUMNS.NAME)+sep)

def set(nb,nm):
	name.set_text(nm)
	z=nm.split(".")
	nb.set_tab_label_text(bx,z[0])
	reqs.requ("list.open",{"filelist" : nm})
	fshow(nm,'')

def backing(b,d):
	s=folder.get_text()
	if not s:
		return
	p=s.rfind(sep,0,-len(sep))
	if p!=-1:
		fshow(name.get_text(),s[:p+len(sep)])
	else:
		fshow(name.get_text(),'')
def fshow(flist,s):
	a=reqs.reque("list.lsdir",{"directory" : s,"filelist" : flist})
	k=a.keys()
	folder.set_text(s)
	list.clear()
	for x in k:
		if "TTH" in a[x]:
			list.append([x,a[x]['TTH']])
		else:
			list.append([x,''])