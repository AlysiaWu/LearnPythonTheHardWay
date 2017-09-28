try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project ex47',
	'author': 'Zhu Xiuwei',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'jlu_zxw@126.coms',
	'version': '0.1',
	'install_requires': [''],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'ex47'
}

setup(**config)