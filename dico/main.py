#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib

def quit(widget, mainloop):
	mainloop.quit()
	return True

def main():
	mainloop = GLib.MainLoop()
	win = Gtk.Window()
	win.connect('close-request', quit, mainloop)
	win.show()
	mainloop.run()

if __name__ == "__main__":
    main()
