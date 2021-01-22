
import gi
from gi.repository import Gtk

def ini(b,win):
	#flg=Gtk.DialogFlags.DESTROY_WITH_PARENT | Gtk.DialogFlags.MODAL
	d=Gtk.Dialog(title="Settings",transient_for=win)
	d.set_modal(True)
	if win.is_maximized():
		d.maximize()
	else:
		dim=win.get_default_size()
		d.set_default_size(dim.width,dim.height)
	d.show()