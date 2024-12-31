##########
MADCUBA IO
##########

Introduction
============

Th key difference between MADCUBA exported cubes and spectra, and those exported
by other programas is how history is written into the files. MADCUBA opts for an
external :ref:`history file <hist_file>` that contains every operation performed
on the data since first imported into MADCUBA.

The IO package of `madcubapy` allows the user to read MADCUBA products like FITS
and *.spec* files alongside their :ref:`history files <hist_file>`.

MadcubaMap
==========

About `~madcubapy.io.madcubamap.MadcubaMap`.

SpectraContainer
================

About `~madcubapy.io.spectracontainer.SpectraContainer`.

``io`` contents
===============

.. toctree::
    :maxdepth: 2

    madcubafits
    madcubamap
    spectracontainer

API Reference
=============

.. toctree::
    :maxdepth: 2

    ref_api
