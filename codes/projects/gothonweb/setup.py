try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'a web game',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'author_email': 'My email',
	'download_url': 'Where to download it',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['flask'],
	'name': 'Gothon'
}

setup(**config)