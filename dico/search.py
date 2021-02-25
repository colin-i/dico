import gi
from gi.repository import Gtk,GLib,GObject

import flist
import reqs
import hubs
import sets
import dload

from enum import IntEnum
class COLUMNS(flist.COLUMNS,IntEnum):
	USERS=len(flist.COLUMNS)
lastcolumn=len(flist.COLUMNS)+len(COLUMNS)

list=eval("Gtk.ListStore("+flist.listcols+",int,GObject.TYPE_BOOLEAN)")
filter=list.filter_new()
sort=Gtk.TreeModelSort.new_with_model(filter)
page=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
info=Gtk.Label()
timer=0
limit=Gtk.EntryBuffer(text="20")

def show():
	scroll=Gtk.ScrolledWindow()
	scroll.set_vexpand(True)
	tree=Gtk.TreeView.new_with_model(sort)
	flist.cols(tree,clk)
	hubs.col(tree,'Users',COLUMNS.USERS,clk)
	filter.set_visible_column(lastcolumn)
	sort.set_sort_column_id(COLUMNS.USERS,Gtk.SortType.DESCENDING)
	tree.connect("row-activated",clkrow,sort)
	tree.set_activate_on_single_click(True)
	scroll.set_child(tree)
	page.append(info)
	page.append(scroll)
	return page
def clk(b,ix):
	hubs.clk_univ(sort,ix)
	reset()
def clkrow(tree,path,column,model):
	dload.add(model,model.get_iter(path))

def reset():
	for x in list:
		list.set_value(x.iter,lastcolumn,True)#to be in filter,then in sort
	limiting()
def start(t):
	reqs.requ("search.send",{"searchstring":t})
def send(e,d):
	t=e.get_text()
	start(t)
	info.set_text(t)
	timer=GLib.timeout_add_seconds(10,get,None)
def close():
	if timer:
		GLib.source_remove(timer)

def append(r):
	for d in list:
		if d[COLUMNS.TTH]==r["TTH"]:
			list.set_value(d.iter,COLUMNS.USERS,d[COLUMNS.USERS]+1)
			return
	list.append([r["Filename"],int(r["Real Size"]),r["TTH"],1,True])#need to be visible at sort for limit
def set():
	list.clear()
	result=reqs.reque("search.getresults",{"huburl":''})#not send final results
	if result:
		for r in result:
			append(r)
		limiting()
def get(d):
	set()
	info.set_text('')
	timer=0
	return False
def limiting():
	n=sort.iter_n_children(None)
	i1=sort.iter_nth_child(None,n-1)
	m=int(limit.get_text())
	for i in range(m,n):
		i2=sort.convert_iter_to_child_iter(i1)
		i3=filter.convert_iter_to_child_iter(i2)
		i1=sort.iter_previous(i1)#not after,critical
		list.set_value(i3,lastcolumn,False)

def store(d):
	d['search_limit']=int(limit.get_text())
def restore(d):
	limit.set_text(str(d['search_limit']),-1)
def confs():
	return sets.entry("Search rows limit",limit)
