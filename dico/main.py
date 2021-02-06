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
import hubs

def quit(widget, mainloop):
	daem.terminate()
	daem.wait()
	base.write(widget)
	limit.close()
	mainloop.quit()
	return True

def main():
	mainloop = GLib.MainLoop()
	win = Gtk.Window()
	win.set_title('Direct Connect')
	base.read(win)
	layout.show(win)
	limit.open(win)
	log.ini()
	stor2.ini()
	hubs.ini()
	win.connect('close-request', quit, mainloop)
	global daem
	dastr='eiskaltdcpp-daemon'#,'-Dv']
	daem=subprocess.Popen(dastr)
	win.show()
	mainloop.run()

if __name__ == "__main__":
    main()
