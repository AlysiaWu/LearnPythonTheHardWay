try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A Test Project',
	'author': 'Zhu Xiuwei',
	'url': 'http://www.zxw.com',
	'download_url': 'http://www.zxw.com/download',
	'author_email': 'jlu_zxw@126.com',
	'version': '0.1',
	'install_requires': [''],
	'packages': ['XwTest'],
	'scripts': [],
	'name': 'XwTestProject'
}

setup(**config)