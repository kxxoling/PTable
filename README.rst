=============
About ptable2
=============

ptable2 is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables, originally
forked from `PTable <https://github.com/kxxoling/PTable/>`_.

.. image:: https://travis-ci.org/madebr/ptable2.svg
    :target: https://travis-ci.org/madebr/ptable2
    :alt: Build Status

.. image:: https://landscape.io/github/madebr/ptable2/master/landscape.svg?style=flat
    :target: https://landscape.io/github/madebr/ptable2/master
    :alt: Code Health

.. image:: https://coveralls.io/repos/github/madebr/ptable2/badge.svg?branch=master
    :target: https://coveralls.io/github/madebr/ptable2?branch=master
    :alt: Coverage


Installation
============

As ptable2 is a fork of PrettyTable, and compatible with all its APIs,
so ptable2 is usage is the same as PrettyTable, and the installation
would cover on the original PrettyTable.

As always, you can install ptable2 in 3 ways.

Via pip (recommend)::

    pip install ptable2

From source::

    python setup.py install


Quick start
===========

ptable2 supports two kinds of usage:


As a library
------------

ptable2 library API is almost as PrettyTable, you can import the same API from
``prettytable`` library:

.. code-block:: python

    from prettytable import PrettyTable
    x = PrettyTable()

A better hosted document is hosted on `ReadTheDocument <http://ptable.readthedocs.org/>`_.


As command-line tool
--------------------

This is an original function of ptable2, can be used as ``ptable`` command:

.. code-block:: shell

    ptable --csv somefile.csv

or a Unix style pipe:

.. code-block:: shell

    cat somefile.csv | ptable

Will both print a ASCII table in terminal.



Relative links
==============

* `Source Code (GitHub) <https://github.com/madebr/ptable2>`__
* `RTFD <https://ptable.readthedocs.org>`__
* `PyPI <https://pypi.python.org/pypi/ptabl://pypi.python.org/pypi/ptable>`__
* `PrettyTable <https://code.google.com/p/prettytable/>`_

