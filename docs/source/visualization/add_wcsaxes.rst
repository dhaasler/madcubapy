.. _add_wcs_axes:

Plotting images with world coordinates
======================================

The :func:`~madcubapy.visualization.add_wcs_axes` an
:func:`~madcubapy.visualization.add_manual_wcs_axes` functions of `madcubapy`
streamline the process of plotting FITS images through the
`~astropy.visualization.wcsaxes.WCSAxes` interface. Both functions accept
`~madcubapy.io.MadcubaMap` and `~astropy.nddata.CCDData` objects, and will parse
information from the FITS headers to automatically set axes and colorbar labels.

Using :func:`~madcubapy.visualization.add_wcs_axes`
---------------------------------------------------

This function adds an axis using the projection stored in the ``wcs`` attribute
of the map object, returning an `~astropy.visualization.wcsaxes.WCSAxes`
object and `~matplotlib.image.AxesImage`.

To use this function, we first need to create an empty figure, and pass it as
an argument alongside the `~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`
object to plot. The function also accepts additional arguments that are passed
to :func:`~matplotlib.pyplot.imshow` such as *cmap*, *vmin*, *vmax*, *norm*, and
many others.

Under the hood, this function behaves the same way as Matplotlib's
:meth:`~matplotlib.figure.Figure.add_subplot`. After the ``figure`` it accepts
three integer values:``nrows``, ``ncols``, and ``index``. The subplot will take the
*index* position on a grid with *nrows* rows and *ncols* columns, with *index*
starting at 1 in the upper left corner and increases to the right.

By default, these numbers are each of them 1, this way, if we do not provide
them, the function adds a `~astropy.visualization.wcsaxes.WCSAxes` object
occupying the entire figure size.

.. note::
    If we call this function using the argument names explicitly, there is no
    need to pass every function argument.
    However, if we are using positional arguments, every parameter must be added
    in order
    (i.e ``add_wcs_axes(fig_object, nrows, ncols, index, map_object)``)
    
    These following statements are all equivalent:

    * ``add_wcs_axes(fig=fig_object, nrows=1, ncols=1, index=1, fitsmap=map_object)``
    * ``add_wcs_axes(fig_object, 1, 1, 1, map_object)``  
    * ``add_wcs_axes(fig=fig_object, fitsmap=map_object)``

Examples
^^^^^^^^
The following code shows how quickly a map can be plotted using `madcubapy`:

.. code-block:: python

    from madcubapy.io import MadcubaMap
    from madcubapy.visualization import add_wcs_axes

    # Read file
    example_file = "examples/data/IRAS16293_SO_2-1_moment0_madcuba.fits"
    madcuba_map = MadcubaMap.read(example_file)

    # Create empty figure
    fig = plt.figure(figsize=(5,5))

    # Add the WCS axes object to the figure. # We can pass kwargs to imshow(),
    # like 'vmin' and 'vmax'.
    ax, img = add_wcs_axes(fig, fitsmap=madcuba_map, vmin=0, vmax=300)

    plt.show()

.. figure:: ../_static/figures/add_wcs_axes_1.png
   :figclass: align-center

The next code generates a figure with two maps aligned horizontaly. Notice that
the *nrows* and *ncols* parameters are 1 and 2, respectively. This way we have
one row and two columns of images. The third number is the **index** value,
going in order left to right. Here the map on the right (number 2) is using
a logarithmic noramlization:

.. code-block:: python

    from madcubapy.io import MadcubaMap
    from madcubapy.visualization import add_wcs_axes

    # Read file
    example_file = "examples/data/IRAS16293_SO_2-1_moment0_madcuba.fits"
    madcuba_map = MadcubaMap.read(example_file)

    # Create empty figure
    fig = plt.figure(figsize=(10,5))

    # Add as many WCS axes objects as desired. We can pass kwargs to imshow()
    ax1, img1 = add_wcs_axes(fig, 1, 2, 1, fitsmap=madcuba_map, vmin=0, vmax=100)
    ax2, img2 = add_wcs_axes(fig, 1, 2, 2, fitsmap=madcuba_map, cmap='jet',
                             vmin=1, vmax=500, norm='log')

    plt.show()

.. figure:: ../_static/figures/add_wcs_axes_2.png
   :figclass: align-center

Using :func:`~madcubapy.visualization.add_manual_wcs_axes`
----------------------------------------------------------

This is a manual version of the :func:`~madcubapy.visualization.add_wcs_axes`
function. It offers the same functionality with one exception: the
`~astropy.visualization.wcsaxes.WCSAxes` object is placed in a manually
selected position instead of a grid.
The location of the subplot is selected via the figure coordinates of its
lower-left corner, alongside its width and height: ``left``, ``bottom``,
``width``, ``height``. Their default values are 0, 0, 1, and 1, respectivelly.

Examples
^^^^^^^^

The previous figure can be recreated using
:func:`~madcubapy.visualization.add_manual_wcs_axes` by placing the left subplot
at the left=0, bottom=0 location with a width of ~half the figure (0.4); and the
right subplot at the left=0.5, bottom=0 location with the same width as before.
Note that the widths are less than half of the figure, and 0.05 has been added
to the ``bottom`` and ``left`` location arguments. This is done to have
sufficient space in the figure to draw the axes ticks and labels, and not have
them cut by the borders.
Also note that the height of the subplots is 1 because the figure size is
already set as 10x5, if we use ~half of the figure height, we would be using
only a height of 2.5 of those 5 available.

.. code-block:: python

    from madcubapy.io import MadcubaMap
    from madcubapy.visualization import add_manual_wcs_axes

    # Read file
    example_file = "examples/data/IRAS16293_SO_2-1_moment0_madcuba.fits"
    madcuba_map = MadcubaMap.read(example_file)

    # Create empty figure
    fig = plt.figure(figsize=(10,5))

    # Add as many WCS axes objects as desired. We can pass kwargs to imshow()
    ax1, img1 = add_manual_wcs_axes(fig, 0.05, 0.05, 0.4, 1, fitsmap=madcuba_map,
                                    vmin=0, vmax=100)
    ax2, img2 = add_manual_wcs_axes(fig, 0.55, 0.05, 0.4, 1, fitsmap=madcuba_map,
                                    cmap='jet', vmin=1, vmax=500, norm='log')

    plt.show()

.. figure:: ../_static/figures/add_manual_wcs_axes_1.png
   :figclass: align-center

This function allows for all sorts of placings:

.. code-block:: python

    from madcubapy.io import MadcubaMap
    from madcubapy.visualization import add_manual_wcs_axes

    # Read file
    example_file = "examples/data/IRAS16293_SO_2-1_moment0_madcuba.fits"
    madcuba_map = MadcubaMap.read(example_file)

    # Create empty figure
    fig = plt.figure(figsize=(7,7))

    # Add as many WCS axes objects as desired. We can pass kwargs to imshow()
    ax1, img1 = add_manual_wcs_axes(fig, 0.05, 0.55, 0.2, 0.2, fitsmap=madcuba_map,
                                    vmin=0, vmax=100)
    ax2, img2 = add_manual_wcs_axes(fig, 0.3, 0.05, 0.5, 0.5, fitsmap=madcuba_map,
                                    vmin=0, vmax=100)
    ax3, img3 = add_manual_wcs_axes(fig, 0.6, 0.65, 0.3, 0.3, fitsmap=madcuba_map,
                                    vmin=0, vmax=100)

    plt.show()

.. figure:: ../_static/figures/add_manual_wcs_axes_2.png
   :figclass: align-center

This is specially useful for sticking two maps right next to the other, by
having one start right where the other ends. Note that we need to hide some axis
labels to prevent overplotting text.

.. code-block:: python

    from madcubapy.io import MadcubaMap
    from madcubapy.visualization import add_manual_wcs_axes

    # Read file
    example_file = "examples/data/IRAS16293_SO_2-1_moment0_madcuba.fits"
    madcuba_map = MadcubaMap.read(example_file)

    # Create empty figure
    fig = plt.figure(figsize=(10,5))

    # Add as many WCS axes objects as desired. We can pass kwargs to imshow()
    ax1, img1 = add_manual_wcs_axes(fig, 0.05, 0.05, 0.4, 1, fitsmap=madcuba_map,
                                    vmin=0, vmax=100)
    ax2, img2 = add_manual_wcs_axes(fig, 0.45, 0.05, 0.4, 1, fitsmap=madcuba_map,
                                    vmin=0, vmax=100)

    # Disable axis label and ticklabels for the right subplot
    ax2.coords[1].set_ticklabel_visible(False)
    ax2.coords[1].set_axislabel(" ", visible=False)
    
    plt.show()

.. figure:: ../_static/figures/add_manual_wcs_axes_3.png
   :figclass: align-center
