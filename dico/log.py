
import gi
from gi.repository import Gtk

file=Gtk.EntryBuffer(text='')
f=None

import sets

def show():
	return sets.entry("Log file location",file)
def store(d):
	d['log_file']=finish()
def restore(d):
	file.set_text(d['log_file'],-1)

def ini():
	log=file.get_text()
	if len(log)>0:
		global f
		f=open(log,"w")

def add(obj):
	if f:
		f.write(obj.__str__()+"\n")
		f.flush()

def finish():
	global f
	if f:
		f.close()
		f=None
	return file.get_text()

def reset():
	d=finish()
	if len(d)>0:
		global f
		f=open(d,"a")
