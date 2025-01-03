.. _philosophy:

###################
Why use `madcubapy`
###################

`madcubapy` simplifies working with FITS files and their accompanying history
files created by MADCUBA. It offers a seamless integration of these files into
Python workflows, enabling efficient data processing and visualization.

The vision of `madcubapy`
=========================

The primary goal of `madcubapy` is to streamline the analysis of
MADCUBA-exported data by combining FITS files and their external history files
into a single, user-friendly object in Python. This avoids the need for manual
parsing and makes the analysis process more intuitive.

MADCUBA Products and the History File
=====================================

Unlike traditional FITS workflows, MADCUBA stores operation details in a
separate "history file" rather than writing them in FITS header cards.
The `madcubapy` package integrates these external history files alongside the
FITS data, ensuring all metadata and processing steps are easily accessible.

For more details, see the dedicated :ref:`History File page<hist_file>`.

Built on Astropy
================

Instead of re-inventing the wheel, `madcubapy` uses the power of the `Astropy`
library for its core functionality.
By building on the `Astropy` ecosystem, `madcubapy` inherits robust, well-tested
features and extends them to meet the specific needs of MADCUBA users.

Why choose `madcubapy`?
=======================

- **Unified Workflow**: Combine FITS and history data into a single Python
  object. Every operation performed on the data through `madcubapy` is stored
  into de history file following MADCUBA standards.
- **Enhanced functionality**: Offers several tools to automatically resolve unit
  inconsistencies and other common issues, even with non-MADCUBA products.
- **Visualization Tools**: Includes helpers for visualizing data created to work
  with `~madcubapy.io.MadcubaMap` objects, but also fully compatible
  with Astropy’s `~astropy.nddata.CCDData` objects.
- **Failsafe mechanism**: The `~madcubapy.io.MadcubaMap` object contains a 
  `~madcubapy.io.MadcubaMap.ccddata` attribute, which is a
  `~astropy.nddata.CCDData` object that can be used for operations that lack
  compatibility with `~madcubapy.io.MadcubaMap` objects.
