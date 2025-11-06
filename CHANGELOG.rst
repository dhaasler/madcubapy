Version 0.8.1 (2025-11-06)
==========================

- Bugfixes:

  - Fix ``_get_integrated_range`` failing if no matching row was found.

Version 0.8.0 (2025-11-02)
==========================

- New features:
  
  - Add possibility to initialize a `MadcubaMap` with a previous ``CCDData``
    object.
  - Add ``update_header_keyword`` method to `MadcubaMap`.
  - Add ``restfreq`` and ``integrated_range`` attributes to `MadcubaMap`.

- Bugfixes:

  - Fix `MadcubaMap` setters not changing the same attributes of the failsafe
    `CCDData` object.
  - Fix `MadcubaMap` initializing the ``hist`` attribute as a reference alias.

Version 0.7.0 (2025-10-28)
==========================

- New features:
  
  - Create ``slim`` module in ``io`` package with the Molecular Parameters
    Tables functions ``import_molecular_parameters_table``,
    ``format_molecular_parameters_columns``, and
    ``output_latex_molecular_parameters_table``.

Version 0.6.5 (2025-10-16)
==========================

- New features:
  
  - Create ``geometry`` module in ``utils`` subpackage with ``polygon_area``,
    ``polygon_signed_area``, and ``calculate_polygon_centroid``.
  - Add a ``sigma`` attribute to ``MadcubaMap``.

- Changes:

  - Change sigma logic in MadcubaMap to be an `astropy.units.Quantity`.
  - Change ``measure_noise`` to use `astropy.units.Quantity`.
  - Rename ``check_contour`` to ``select_contour_regions``.
  - Rename ``all_in_one`` to ``check_sigma_contours``.

- Bugfixes:

  - Fix ``MadcubaMap.convert_unit_to()`` not storing the new unit onto the
    BUNIT header keyword.

Version 0.6.1 (2025-04-30)
==========================

- Bugfixes:

  - Fix incorrect right-click index recognition using scripts in macOS.

Version 0.6.0 (2025-04-30)
==========================

- New features:

  - Add ``spectral`` module to `coordinates` package with ``SpectralData``
    class.
  - Add spectral data conversions functions to `utils.spectral` module.

Version 0.5.6 (2025-04-10)
==========================

- Bugfixes:

  - Fix incorrect dtype initialization when reading incomplete history files.

Version 0.5.5 (2025-03-25)
==========================

- New features:

  - Add ``contours`` module to `regions` package with ``check_contour``,
    ``import_region_contourset``, and ``import_region_patch`` functions.

Version 0.5.0 (2025-03-24)
==========================

- New features:

  - Create `regions` package to work with MADCUBA, pyroi, CRTF, and DS9 rois
    with ``import_roi`` and ``export_roi`` functions.

Version 0.4.5 (2025-03-21)
==========================

- New features:

  - Create `coordinates` > ``conversions`` module with ``fits_to_python``,
    ``python_to_fits``, ``world_to_pixel``, ``pixel_to_world``,
    ``angle_to_pixels``, and ``pixels_to_angle`` functions.

Version 0.4.0 (2025-03-19)
==========================

- New features:

  - Create `coordinates` subpackage.
    
    - Crete transforms module with ``transform_coords_axes`` and
      ``transform_coords_fitsmap`` functions.

    - Add ``copy_zoom_axes``, ``copy_zoom_fitsmap``, and ``sync_zoom`` to
      ``visualization`` package.

- Changes:

  - Move and geometry module from utils into coordinates > offsets.

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
