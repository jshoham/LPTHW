# ex46
# setup.py

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author' : 'Jake Shoham',
	'url' : 'blank',
	'download_url' : 'blank',
	'author_email' : 'jakeonyx@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['NAME'],
	'scripts' : [],
	'name' : 'projectname'
	}
	
setup(**config)