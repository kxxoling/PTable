============
About PTable
============

PTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables, originally
forked from `PrettyTable <https://code.google.com/p/prettytable/>`_.

.. image:: https://travis-ci.org/kxxoling/PTable.svg
    :target: https://travis-ci.org/kxxoling/PTable
    :alt: Build Status

.. image:: https://landscape.io/github/kxxoling/PTable/master/landscape.svg?style=flat
    :target: https://landscape.io/github/kxxoling/PTable/master
    :alt: Code Health

.. image:: https://coveralls.io/repos/github/kxxoling/PTable/badge.svg?branch=master
    :target: https://coveralls.io/github/kxxoling/PTable?branch=master
    :alt: Coverage


Installation
============

As PTable is a fork of PrettyTable, and compatible with all its APIs,
so PTable is usage is the same as PrettyTable, and the installation
would cover on the original PrettyTable.

As always, you can install PTable in 3 ways.

Via pip (recommend)::

    pip install PTable

Via easy_install::

    easy_install PTable

From source::

    python setup.py install


Quick start
===========

PTable supports two kinds of usage:


As a library
------------

PTable library API is almost as PrettyTable, you can import the same API from
``prettytable`` library:

.. code-block:: python

    from prettytable import PrettyTable
    x = PrettyTable()

A better hosted document is hosted on `ReadTheDocument <http://ptable.readthedocs.org/>`_.


As command-line tool
--------------------

This is an original function of PTable, can be used as ``ptable`` command:

.. code-block:: shell

    ptable --csv somefile.csv

or a Unix style pipe:

.. code-block:: shell

    cat somefile.csv | ptable

Will both print a ASCII table in terminal.



Relative links
==============

* `Source Code (GitHub) <https://github.com/kxxoling/PrettyTable>`__
* `RTFD <https://ptable.readthedocs.org>`__
* `PyPI <https://pypi.python.org/pypi/ptabl://pypi.python.org/pypi/ptable>`__
* `PrettyTable <https://code.google.com/p/prettytable/>`_

