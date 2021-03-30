import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

from setuptools import setup
setup(name='dico',
	install_requires=["PyGObject>=3.40","requests>=2.21"],
	version='1.0.0',
	description='Direct Connect ++ client',
	long_description=README,
	long_description_content_type="text/markdown",
	url='https://github.com/colin-i/dico',
	author='bot',
	author_email='costin.botescu@gmail.com',
	license='MIT',
	packages=['dico'],
	package_data={'dico': ['hublist.xml']},
	include_package_data=True,
	zip_safe=False,
	entry_points = {
		'console_scripts': ['dico=dico.main:main']
	}
)
