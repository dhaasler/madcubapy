.. _info_slim:

##########
SLIM Tools
##########

The `madcubapy.io` package includes classes and functions to work with
products from the Spectral Line Identification and Modelling (SLIM) tool of
MADCUBA.

Molecular Parameters Tables
===========================

The SLIM Tool of MADCUBA lets the user export the molecular parameters of the
analysis by hitting *SLIM Product > Save Molecular Parameters*. This table can
be exported in several formats, of which ASCII and CSV are compatible with
`madcubapy`.

Read Molecular Parameters Tables
--------------------------------

The :func:`~madcubapy.io.import_molecular_parameters_table` imports a Molecular
Parameters Table as a `~astropy.table.Table` and applies some basic
organization for a set of molecules **(currently fixed in the code)** by ading two
columns named ``Formula_short`` and ``Label`` to help the user select
molecules in the analysis and plotting of parameters.

>>> from madcubapy.io import import_molecular_parameters_table
>>> t = import_molecular_parameters_table("input_file.txt", format='ascii')
>>> t = import_molecular_parameters_table("input_file.csv", format='csv')

Export Molecular Parameters Tables formatted for LaTex
------------------------------------------------------

The :func:`~madcubapy.io.output_latex_molecular_parameters_table` function
exports a Molecular Parameters Table with LaTeX formatting into a text file.

>>> output_latex_molecular_parameters_table(t, "latex.txt")

This function does not simply create a table using LaTeX syntax, at which
`astropy` already does a good job. This function formats every parameter column
to output the corresponding significant values when appropriate.
For fixed parameters without uncertainty, it performs an in depth comparison
between molecules and velocity components to discover the reason for the
parameter being fixed, whether it is a fixed velocity component from a
different molecule, or an excitation temperature fixed from a different
velocity component.

This formatting can also be applied to a Molecular Parameters Table without
exporting it.
The :func:`~madcubapy.io.format_molecular_parameters_columns` function creates
new columns for each molecular parameter with the corresponding formatted
strings.

>>> formatted_t = format_molecular_parameters_columns(t)