import gi
from gi.repository import GLib,Gtk

import reqs

time=1
#limit=1
timer=0

def open(win):
	if time>0:
		global timer
		timer=GLib.timeout_add_seconds(time*60,callba,win)

def close():
	global timer
	if timer:
		GLib.source_remove(timer)
		timer=0

def callba(win):
	res=reqs.req("show.ratio")
	if int(res['up_bytes'])>(10):
		global timer
		timer=0
		win.close()
		return False
	return True

def sets():
	f=Gtk.Frame()
	f.set_label("Close program when upload is greater than Value in bytes")
	g=Gtk.Grid()
	lb=Gtk.Label()
	lb.set_halign(Gtk.Align.START)
	lb.set_text("Interval time to verify in minutes (0=disable)")
	g.attach(lb,0,0,1,1)
	en=Gtk.Entry()
	en.set_hexpand(True)
	g.attach(en,1,0,1,1)
	lb=Gtk.Label()
	lb.set_halign(Gtk.Align.START)
	lb.set_text("Value")
	g.attach(lb,0,1,1,1)
	en=Gtk.Entry()
	en.set_hexpand(True)
	g.attach(en,1,1,1,1)
	f.set_child(g)
	return f