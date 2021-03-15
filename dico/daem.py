
from gi.repository import Gtk

data=Gtk.EntryBuffer()#text=''

from . import sets
from . import hubscon
from . import main

def confs():
	global keep
	keep=data.get_text()
	return sets.entry("Daemon parameters",data)
def store(d):
	d['daemon_args']=data.get_text()
def restore(d):
	data.set_text(d['daemon_args'],-1)
def reset():
	if keep!=data.get_text():
		main.dclose()
		restart()

def restart():
	main.dopen()
	hubscon.recon()
