from setuptools import setup

setup(name='dico',
      version='0.1',
      description='Direct Connect client',
      url='https://github.com/colin-i/dico',
      author='bot',
      author_email='costin.botescu@gmail.com',
      license='MIT',
      packages=['dico'],
      zip_safe=False,
      entry_points = {
          'console_scripts': ['dico=dico.main:main']
      }
)
