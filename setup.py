#!/usr/bin/env python
from setuptools import setup
from prettytable import __version__ as version


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()


setup(
    name='ptable2',
    version=version,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ptable = prettytable.cli:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: BSD License',
        'Topic :: Text Processing'
    ],
    license="BSD (3 clause)",
    description='A simple Python library for easily displaying tabular data in a visually appealing ASCII table format',
    long_description=fread('README.rst'),
    author='Luke Maurits',
    author_email='luke@maurits.id.au',
    maintainer='Maarten',
    maintainer_email='anonymous.maarten@gmail.com',
    url='https://github.com/madebr/ptable2',
    py_modules=['prettytable', 'prettytable.cli', 'prettytable.prettytable',
                'prettytable.factory', 'prettytable._compact'],
    test_suite="test_prettytable",
)
