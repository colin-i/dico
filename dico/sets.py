
import gi
from gi.repository import Gtk

def ini(b,win):
	d=Gtk.Dialog(title="Settings",transient_for=win)
	#,flags=Gtk.DialogFlags.DESTROY_WITH_PARENT | Gtk.DialogFlags.MODAL)
	d.show()