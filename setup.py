#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from os.path import join, dirname, abspath
import sys
from setuptools import setup, find_packages

PY2 = sys.version_info[0] == 2


def read_relative_file(filename):
    """Returns contents of the given file, whose path is supposed relative
    to this module."""
    path = join(dirname(abspath(__file__)), filename)
    with io.open(path, encoding='utf-8') as f:
        return f.read()


NAME = 'workalendar'
DESCRIPTION = 'Worldwide holidays and working days helper and toolkit.'
REQUIREMENTS = [
    'python-dateutil',
    'lunardate',
    'pytz',
    'pyCalverter',
    'setuptools>=1.0',
]
version = '2.4.0.dev0'
__VERSION__ = version

if PY2:
    REQUIREMENTS.append('pyephem')
else:
    REQUIREMENTS.append('ephem')

params = dict(
    name=NAME,
    description=DESCRIPTION,
    packages=find_packages(),
    version=__VERSION__,
    long_description=read_relative_file('README.rst'),
    author='Bruno Bord',
    author_email='bruno.bord@people-doc.com',
    url='https://github.com/peopledoc/workalendar',
    license='MIT License',
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

if __name__ == '__main__':
    setup(**params)
