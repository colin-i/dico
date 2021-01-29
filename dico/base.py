import os.path
import json

import limit
import log
import stor2
import hubs

def get_root_conf():
	return get_root_file('config.json')
def get_root_file(f):
	return os.path.join(os.path.dirname(os.path.realpath(__file__)),f)

def write(win):
	d={}
	dim=win.get_default_size()
	d['width']=dim.width
	d['height']=dim.height
	d['max']=win.is_maximized()
	limit.store(d)
	log.store(d)
	stor2.store(d)
	hubs.store(d)
	with open(get_root_conf(), "w") as write_file:
		json.dump(d, write_file)

def read(win):
	try:
		with open(get_root_conf()) as f:
			d=json.load(f)
			win.set_default_size(d['width'],d['height'])
			if(d['max']):
				win.maximize()
			limit.restore(d)
			log.restore(d)
			stor2.restore(d)
			hubs.restore(d)
	except Exception:
		pass