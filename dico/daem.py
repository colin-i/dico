
import gi
from gi.repository import Gtk

data=Gtk.EntryBuffer(text='')

from . import sets
from . import hubscon
from . import main

def confs():
	return sets.entry("Daemon parameters",data)
def store(d):
	d['daemon_args']=data.get_text()
def restore(d):
	data.set_text(d['daemon_args'],-1)
def reset():
	main.dclose()
	restart()

def restart():
	main.dopen()
	hubscon.recon()
