# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in rotary_online/__init__.py
from rotary_online import __version__ as version

setup(
	name='rotary_online',
	version=version,
	description='ERP for Rotary District Organizations',
	author='Neil Lasrado, Rotaract Charitable Trust',
	author_email='neil@rotaract3142.org',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
