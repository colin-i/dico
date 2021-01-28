
import gi
from gi.repository import Gtk

file=Gtk.EntryBuffer(text='')
f=None

def sets():
	bx=Gtk.Box()
	lb=Gtk.Label()
	lb.set_halign(Gtk.Align.START)
	lb.set_text("Log file location")
	bx.append(lb)
	en=Gtk.Entry.new_with_buffer(file)
	en.set_hexpand(True)
	bx.append(en)
	return bx

def store(d):
	d['log_file']=finish()
def restore(d):
	log=d['log_file']
	if len(log)>0:
		file.set_text(log,-1)
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
