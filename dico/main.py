#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib
import subprocess
import shlex

from . import base
from . import layout 
from . import limit
from . import log
from . import stor2
from . import nick
from . import hubs
from . import hubscon
from . import daem
from . import search
from . import dload
from . import com

def dopen():
	seq=shlex.split(daem.data.get_text())
	args=['eiskaltdcpp-daemon']
	for s in seq:
		args.append(s)
	nick.daeminst=subprocess.Popen(args)#otherwise, cannot make it works
def dclose():
	nick.daeminst.terminate()
	nick.daeminst.wait()
def quit(widget, mainloop):
	base.write(widget)
	dclose()#in base.write is log, can require daemon open
	limit.close()
	hubscon.close()
	search.close()
	dload.close()
	com.close()
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
