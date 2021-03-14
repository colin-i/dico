import gi
from gi.repository import Gtk,GLib,GObject

from . import flist
from . import reqs
from . import hubs
from . import dload
from . import details
from . import extension

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
extensions=Gtk.EntryBuffer()#text=""

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
	if len(filter)>0:
		resort()
def clkrow(tree,path,column,model):
	it=model.get_iter(path)
	dload.add(model,it)
	details.set(model.get_value(it,COLUMNS.DETAIL))

def reset():
	reshow()
	relimiting()
def resort():
	reshow()
	limiting()
def relimiting():
	if len(filter)>0:
		limiting()
def reshow():
	for x in list:
		nm=list.get_value(x.iter,flist.COLUMNS.NAME)
		list.set_value(x.iter,lastcolumn,extension_filter(nm))#to be in filter,then in sort
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
	nm=r["Filename"]
	list.append([nm,int(r["Real Size"]),r["TTH"],1,0 if fr=="0" else 1,[details.create(r,fr)],extension_filter(nm)])#need to be visible at sort for limit
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
		relimiting()
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
def extension_filter(nm):
	ext=extensions.get_text()
	if ext:
		p=nm.rfind('.')
		if p==-1:
			return False
		ex=nm[p+1:]
		e=ext.split(";")
		for x in e:
			if x==ex:
				return True
		return False
	return True

def store(d):
	d['search_limit']=int(limit.get_text())
	extension.store(d)
def restore(d):
	limit.set_text(str(d['search_limit']),-1)
	extension.restore(d)
def confs(win):
	f=Gtk.Frame(label="Search options")
	g=Gtk.Grid()
	lb=Gtk.Label(halign=Gtk.Align.START,label="Rows limit")
	g.attach(lb,0,0,1,1)
	en=Gtk.Entry(buffer=limit,hexpand=True)
	g.attach(en,1,0,1,1)
	lb=Gtk.Label(halign=Gtk.Align.START,label="Extensions (e1;e2...eN or unfiltered(blank))")
	g.attach(lb,0,1,1,1)
	en=Gtk.Entry(buffer=extensions,hexpand=True)
	g.attach(extension.confs(en,win),1,1,1,1)
	f.set_child(g)
	return f
