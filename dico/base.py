import os.path
import json

import limit

def get_root_file():
	return os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.json')

def write(win):
	d={}
	dim=win.get_default_size()
	d['width']=dim.width
	d['height']=dim.height
	d['max']=win.is_maximized()
	limit.store(d)
	with open(get_root_file(), "w") as write_file:
		json.dump(d, write_file)

def read(win):
	try:
		with open(get_root_file()) as f:
			d=json.load(f)
			win.set_default_size(d['width'],d['height'])
			if(d['max']):
				win.maximize()
			limit.restore(d)
	except Exception:
		pass