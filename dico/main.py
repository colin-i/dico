#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib

def main():
	mainloop = GLib.MainLoop()
	win = Gtk.Window()
	win.show()
	mainloop.run()

if __name__ == "__main__":
    main()
