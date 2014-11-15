#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='vimix',
    version='0.0.1',
    packages=find_packages(),
    scripts = ['scripts/vimix'],

    package_data = {
        'templates': ['*.txt'],
    },

    author='boku',
    author_email='punipuniomochi@gmail.com',
    description='Make minimum environment for Vim script',
    license = 'WTFPL',
    url='https://github.mtwtkman/vimix',

    entry_points = {
        'console_scripts': ['vimix = vimix:main']
    }
)
