
from gi.repository import Gtk
import appdirs
import os
import psutil
import shlex
import subprocess
import sys

data=Gtk.EntryBuffer()#text=''

from . import sets
from . import hubscon
from . import reqs
from . import stor2

name='eiskaltdcpp-daemon'
instobj=None

def ini():
	if sys.platform=='win32':
		global name
		name='eiskaltdcpp-daemon.exe'
		#stor2.name=appdirs.user_config_dir('EiskaltDC++',None,roaming=True)
		a=appdirs.user_config_dir('EiskaltDC++',roaming=True)
		stor2.name=os.path.dirname(a)
	else:
		stor2.name=appdirs.user_config_dir('eiskaltdc++')
def confs():
	global keep
	keep=data.get_text()
	return sets.entry("Daemon parameters",data)
def store(d):
	d['daemon_args']=data.get_text()
def restore(d):
	data.set_text(d['daemon_args'],-1)
def reset():
	if keep!=data.get_text():
		dclose()
		restart()

def restart():
	open()
	hubscon.recon()

def runs():
	for proc in psutil.process_iter():
		try:#/y/x proc.name() = x
			if name==proc.name():
				return proc
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return None
def dopen():
	global absent
	absent=runs()==None
	if absent:
		try:
			open()
		except Exception:
			if os.path.exists("/etc/os-release"):
				import builtins
				with builtins.open("/etc/os-release") as f:
					if "ID=fedora" in f.read().splitlines():
						print('sudo dnf install eiskaltdcpp')
			raise
def dclose():
	close(True)
def dclose_owned():
	close(False)
def open():
	seq=shlex.split(data.get_text())
	args=[name]
	for s in seq:
		args.append(s)
	global instobj
	instobj=subprocess.Popen(args)
def close(inter):
	try:
		t=10
		if absent:
			instobj.terminate()
			instobj.wait(timeout=t)
		elif inter:
			if instobj:
				instobj.terminate()
				instobj.wait(timeout=t)
			else:
				p=psutil.Process(runs().pid)
				reqs.req("daemon.stop")
				p.wait(timeout=t)
	except subprocess.TimeoutExpired:
		print("timeout at daemon close")
#-11 (SIGSEGV)
#			instobj.communicate() is same
#			terminate is SIGTERM, SIGINT or daemon.stop is same
#apport is catching first two tries
