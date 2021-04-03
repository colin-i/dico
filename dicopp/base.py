import json
import appdirs
import os.path
import pathlib

from gi.repository import Gdk

from . import limit
from . import log
from . import stor2
from . import nick
from . import hubs
from . import hubson
from . import search
from . import daem
from . import dload
from . import com

def get_root_conf():
	p=pathlib.Path(appdirs.user_config_dir('dicopp'))
	p.mkdir(exist_ok=True)
	return os.path.join(p,'config.json')

def write(win):
	d={}
	dim=win.get_default_size()
	d['width']=dim.width
	d['height']=dim.height
	d['max']=win.is_maximized()
	d['min']=win.get_surface().get_state()&Gdk.ToplevelState.MINIMIZED
	limit.store(d)
	log.store(d)
	stor2.store(d)
	nick.store(d)
	hubs.store(d)
	hubson.store(d)
	search.store(d)
	daem.store(d)
	dload.store(d)
	com.store(d)
	with open(get_root_conf(), "w") as write_file:
		json.dump(d, write_file)

def read(win):
	try:
		with open(get_root_conf()) as f:
			d=json.load(f)
			win.set_default_size(d['width'],d['height'])
			if(d['max']):
				win.maximize()
			if(d['min']):
				win.minimize()
			limit.restore(d)
			log.restore(d)
			stor2.restore(d)
			nick.restore(d)
			hubs.restore(d)
			search.restore(d)
			daem.restore(d)
			dload.restore(d)
			com.restore(d)
			return d
	except Exception:
		return None
def read2(d):
	if d:
		hubson.restore(d)
