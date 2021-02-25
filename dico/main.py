#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib
import subprocess

import base
import layout 
import limit
import log
import stor2
import nick
import hubs
import hubscon
import daem
import search
import dload

def dopen():
	args=['eiskaltdcpp-daemon',daem.data.get_text()]
	nick.daem=subprocess.Popen(args)#otherwise, cannot make it works
def dclose():
	nick.daem.terminate()
	nick.daem.wait()
def quit(widget, mainloop):
	dclose()
	base.write(widget)
	limit.close()
	hubscon.close()
	search.close()
	dload.close()
	mainloop.quit()
	return True

def main():
	mainloop = GLib.MainLoop()
	win = Gtk.Window()
	win.set_title('Direct Connect')
	d=base.read(win)
	layout.show(win)
	limit.open(win)
	log.ini()
	stor2.ini()
	nick.ini(False)
	hubs.ini()
	win.connect('close-request', quit, mainloop)
	dopen()
	base.read2(d)#after daemon start
	win.show()
	mainloop.run()

if __name__ == "__main__":
    main()
