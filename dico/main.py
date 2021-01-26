#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib
import subprocess

import base
import limit
import layout 
import stor2

def quit(widget, mainloop):
	base.write(widget)
	mainloop.quit()
	limit.close()
	daem.terminate()
	daem.wait()
	return True

def main():
	mainloop = GLib.MainLoop()
	win = Gtk.Window()
	win.set_title('Direct Connect')
	base.read(win)
	limit.open(win)
	stor2.ini()
	win.connect('close-request', quit, mainloop)
	global daem
	daem=subprocess.Popen('eiskaltdcpp-daemon')#,'-Dv']
	layout.show(win)
	win.show()
	mainloop.run()

if __name__ == "__main__":
    main()
