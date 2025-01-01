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
