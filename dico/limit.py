import gi
from gi.repository import GLib

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
