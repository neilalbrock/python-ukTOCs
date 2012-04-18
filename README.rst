=============================================
python-ukTOCs - Standalone UK TOC definitions
=============================================

:Author: Neil Albrock
:Version: 0.1.0

There are 24 train operating companies in the UK, ATOC assigns a code for each which
is used to reference them in systems and data files.
``python-ukTOCs`` is a self contained module that converts between these codes and the
TOC names, as well as providing some addtional useful information.

Installation
============

::

    $ pip install ukTOCs
    

Usage
=====

::

    >>> from ukTOCs import tocs
    >>>
    >>> tocs.get('SR')
    TOC(code='SR', name='ScotRail')