Version 0.3.1 (2025-03-18)
==========================

- Bugfixes:
  
  - Fix swapping right-middle mouse buttons depending on system OS.

Version 0.3.0 (2025-03-18)
==========================

- New features:

  - Create ``geometry module in utils subpackage`` with
    ``get_angle_offset_point``, ``get_angle_separation``,
    ``get_physical_offset_point``, ``get_physical_separation`` functions.

Version 0.2.1 (2025-03-15)
==========================

- Changes:

  - Add compatibility of ``add_colorbar`` and ``insert_colorbar`` with
    ``matplotlib.axes.Axes``.

Version 0.2.0 (2025-02-11)
==========================

- New features:

  - Add ``measure_noise`` function.

    - Add an ``update_sigma`` method to ``MadcubaMap`` to measure the noise and
      save it in the FITS header.

  - Add interaction module with ``get_input`` function.
    
    - Add a ``get_input`` method to ``MadcubaMap`` to do the same.
  
  - Add ``show()`` method to ``MadcubaMap``.

- Changes:

  - Rename ``append_colorbar`` to ``insert_colorbar``.
  - Change ``width`` parameter to ``size`` in ``add_colorbar`` and
    ``append_colorbar``.
  - ``MadcubaMap`` method ``convert_unit_to`` now converts the SIGMA header
    card if present.

Version 0.1.0 (2024-12-13)
==========================

- Finish main functionality for Madcuba fits maps.

  - ``read()`` and ``write()`` methods implementations.
  - Automatic history file updating.

- Add ``filename`` attribute to ``MadcubaMap`` and ``SpectraContainer`` to allow
  tracking.
  
- Create functions to operate on map data.

  - Add the emission of any given number of maps with ``stack_emission``.

Version 0.0.5 (2024-12-02)
==========================

- Add ``copy()`` methods to ``MadcubaMap`` and ``SpectraContainer``.
- Add ``quick_show()`` and ``are_equal()`` functions.
- Add unit conversor for ``MadcubaMap``.

Version 0.0.4 (2024-11-29)
==========================

Add ``fix_units()`` method to fix incorrectly parsed units in a ``MadcubaMap``. 


Version 0.0.3 (2024-11-28)
==========================

Add hist table updater to ``MadcubaFits``, to write new history into the file.


Version 0.0.2 (2024-11-27)
==========================

Added ``add_wcs_axes()``, ``add_manual_wcs_axes()``, ``append_colorbar()``, and
``add_colorbar()`` helper functions to plot ``MadcubaMaps`` and ``CCDData``
objects using astropy's ``WCSAxes``.


Version 0.0.1 (2024-11-25)
==========================

Initial release with ``MadcubaFits``, ``MadcubaMap``, and ``SpectraContainer``
classes containing main attributes: ``data``, ``unit``, ``header``, ``wcs``,
``ccddata``, and ``hist`` for ``MadcubaMap``; and ``bintable`` and ``hist`` for
``SpectraContainer``.
