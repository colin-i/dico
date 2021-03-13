import gi
from gi.repository import Gtk,GLib,GObject

from . import flist
from . import reqs
from . import hubs
from . import sets
from . import dload
from . import details

from enum import IntEnum
class COLUMNS(flist.COLUMNS,IntEnum):
	USERS=len(flist.COLUMNS)
	FUSERS=USERS+1
	DETAIL=FUSERS+1
lastcolumn=len(flist.COLUMNS)+len(COLUMNS)

list=eval("Gtk.ListStore("+flist.listcols+",int,int,GObject.TYPE_PYOBJECT,GObject.TYPE_BOOLEAN)")
filter=list.filter_new()
sort=Gtk.TreeModelSort.new_with_model(filter)
page=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
info=Gtk.Label()
timer=0
limit=Gtk.EntryBuffer(text="20")
flag=False

def show():
	scroll=Gtk.ScrolledWindow()
	scroll.set_vexpand(True)
	tree=Gtk.TreeView.new_with_model(sort)
	flist.cols(tree,clk)
	hubs.col(tree,'Users',COLUMNS.USERS,clk)
	hubs.col(tree,'Users with Free Slots',COLUMNS.FUSERS,clk)
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
	it=model.get_iter(path)
	dload.add(model,it)
	details.set(model.get_value(it,COLUMNS.DETAIL))

def reset():
	if len(list)>0:
		for x in list:
			list.set_value(x.iter,lastcolumn,True)#to be in filter,then in sort
		limiting()
def start(t):
	reqs.requ("search.send",{"searchstring":t})
def send(e,nb):
	t=e.get_text()
	start(t)
	info.set_text(t)
	nr=nb.page_num(page)
	if nb.get_current_page()!=nr:
		global flag
		flag=True
		nb.set_current_page(nr)
	close()
	timer=GLib.timeout_add_seconds(10,get,None)
def close():
	if timer:
		GLib.source_remove(timer)

def append(r):
	fr=r["Free Slots"]
	for d in list:
		if d[COLUMNS.TTH]==r["TTH"]:
			list.set_value(d.iter,COLUMNS.USERS,d[COLUMNS.USERS]+1)
			if fr!="0":
				list.set_value(d.iter,COLUMNS.FUSERS,d[COLUMNS.FUSERS]+1)
			details.update(r,fr,list,d.iter,COLUMNS.DETAIL)
			return
	list.append([r["Filename"],int(r["Real Size"]),r["TTH"],1,0 if fr=="0" else 1,[details.create(r,fr)],True])#need to be visible at sort for limit
def set():
	global flag
	if flag:
		flag=False
	else:
		setcomplex()
def setcomplex():
	list.clear()
	result=reqs.reque("search.getresults",{"huburl":''})#not send final results
	if result:
		for r in result:
			if "TTH" in r:#not working with Directory ,yet
				append(r)
		if len(list)>0:
			limiting()
def get(d):
	setcomplex()
	info.set_text('')
	timer=0
	return False
def limiting():
	n=sort.iter_n_children(None)
	m=n-1
	n-=int(limit.get_text())
	for i in range(0,n):
		i1=sort.iter_nth_child(None,m-i)
		i2=sort.convert_iter_to_child_iter(i1)
		i3=filter.convert_iter_to_child_iter(i2)
		list.set_value(i3,lastcolumn,False)

def store(d):
	d['search_limit']=int(limit.get_text())
def restore(d):
	limit.set_text(str(d['search_limit']),-1)
def confs():
	return sets.entry("Search rows limit",limit)
