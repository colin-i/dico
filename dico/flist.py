import gi
from gi.repository import Gtk

import reqs
import hubs

from enum import IntEnum
class COLUMNS(IntEnum):
	NAME=0
	SIZE=1
	TTH=2

name=Gtk.Label()
folder=Gtk.Label()
bx=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
listcols="str,int,str"
list=eval("Gtk.ListStore("+listcols+")")
sort=Gtk.TreeModelSort.new_with_model(list)
sep="\\"

def cols(tree,act):
	hubs.col(tree,'Name',COLUMNS.NAME,act)
	hubs.col(tree,'Size',COLUMNS.SIZE,act)
	hubs.col(tree,'TTH',COLUMNS.TTH,act)
def show():
	scroll=Gtk.ScrolledWindow()
	scroll.set_vexpand(True)
	tree=Gtk.TreeView.new_with_model(sort)
	cols(tree,clk)
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
		e=a[x]
		if "TTH" in e:
			t=e['TTH']
		else:
			t=''
		list.append([x,int(e['Size']),t])
