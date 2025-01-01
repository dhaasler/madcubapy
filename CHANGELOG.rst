Version 0.1.0 (2024-12-13)
==========================

- Finish main functionality for Madcuba fits maps.

  - ``read()`` and ``write()`` methods implementations.
  - Automatic history file updating.

- Add 'filename' attribute to MadcubaMap and SpectraContainer to allow tracking.
  
- Create functions to operate on map data.

  - Add the emission of any given number of maps with ``stack_emission``

Version 0.0.5 (2024-12-02)
==========================

- Add copy methods to MadcubaMap and SpectraContainer.
- Add quick_show and are_equal functions.
- Add unit conversor for MadcubaMap.
- Add method to fix incorrectly coded BUNIT.

Version 0.0.4 (2024-11-29)
==========================

Add method to fix incorrectly parsed units in a MadcubaMap. 


Version 0.0.3 (2024-11-28)
==========================

Add hist table updater to MadcubaFits, to write new history into the file.


Version 0.0.2 (2024-11-27)
==========================

Added helper functions to plot MadcubaMaps and CCDData objects on WCSAxes.


Version 0.0.1 (2024-11-25)
==========================

Initial release with ``MadcubaFits``, ``MadcubaMap``, and `~madcubapy.io.spectracontainer.SpectraContainer` classes
containing every .
