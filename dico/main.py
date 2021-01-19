#!/usr/bin/env python3

import gi
import subprocess

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib

import base
import limit

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
	win.connect('close-request', quit, mainloop)
	global daem
	daem=subprocess.Popen('eiskaltdcpp-daemon')#,'-Dv']
	win.show()
	mainloop.run()

if __name__ == "__main__":
    main()
