import gi
from gi.repository import Gtk,GLib

import flist
import reqs
import hubs

from enum import IntEnum
class COLUMNS(flist.COLUMNS,IntEnum):
	USERS=len(flist.COLUMNS)

list=eval("Gtk.ListStore("+flist.listcols+",int)")
sort=Gtk.TreeModelSort.new_with_model(list)
page=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
info=Gtk.Label()
timer=0

def show():
	scroll=Gtk.ScrolledWindow()
	scroll.set_vexpand(True)
	tree=Gtk.TreeView.new_with_model(sort)
	flist.cols(tree,clk)
	hubs.col(tree,'Users',COLUMNS.USERS,clk)
	scroll.set_child(tree)
	page.append(info)
	page.append(scroll)
	return page
def clk(b,ix):
	hubs.clk_univ(sort,ix)

def send(e,d):
	t=e.get_text()
	reqs.requ("search.send",{"searchstring":t})
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
	list.append([r["Filename"],r["TTH"],1])
def getresults():
	list.clear()
	result=reqs.reque("search.getresults",{"huburl":''})#not send final results
	if result:
		for r in result:
			append(r)
def get(d):
	getresults()
	info.set_text('')
	timer=0
	return False