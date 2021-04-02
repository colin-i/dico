#setuptools.setup is looking at one argv parameter; to "build" and "install":
#python3 setup.py install

pkname='dicopp'

import subprocess
import sys
test=subprocess.run([sys.executable,'-m','pip','install','PyGObject>=3.40'])
if test.returncode:
	exit(test.returncode)
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib,GObject,Gdk
test=subprocess.Popen(['eiskaltdcpp-daemon'])
test.terminate()
test.wait()

import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

from setuptools import setup
setup(name=pkname,
	install_requires=["PyGObject>=3.40","requests>=2.21"],#gobj is here for bdist_wheel and sdist(visual,building wheels is nonverbose)
	version='1.0.3',
	description='Direct Connect ++ client',
	long_description=README,
	long_description_content_type="text/markdown",
	url='https://github.com/colin-i/dico',
	author='bot',
	author_email='costin.botescu@gmail.com',
	license='MIT',
	packages=[pkname],
	package_data={pkname: ['hublist.xml']},
	include_package_data=True,
	zip_safe=False,
	entry_points = {
		'console_scripts': [pkname+'='+pkname+'.main:main']
	}
)
