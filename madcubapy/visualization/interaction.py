from astropy.nddata import CCDData
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

from madcubapy.io import MadcubaMap
from .wcsaxes_helpers import add_wcs_axes
from .wcsaxes_helpers import insert_colorbar

__all__ = [
    'measure_noise',
    'get_input',
]


def measure_noise(
        fitsmap,
        statistic='std',
        **kwargs):
    """
    Measure the noise (sigma) in a map object by calculating the standard
    deviation (std) or root mean squared (rms) inside several polygons selected
    by mouse clicks.

    - Left clicks create polygon vertices.
    - Right click closes the current polygon, and a subsequent left click
      starts a new polygon.

    Parameters
    ----------
    fitsmap : `~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`
        Map object to analize.
    statistic : {'std', 'rms'}, optional
        Statistic to be used as sigma. Defaults to 'std' and can be changed at
        runtime via GUI buttons.

    Returns
    -------
    sigma : `float`
        Measured noise of the image in the same units as the data array.

    Other Parameters
    ----------------
    **kwargs
        Optional map visualization parameters passed to
        :func:`~madcubapy.visualization.add_wcs_axes`.

    """

    if statistic != 'std' and statistic != 'rms':
        raise ValueError(f"Invalid input for statistic: '{statistic}'. "
                         + "Accepted values are 'std' or 'rms'.")

    if ('use_std' not in kwargs and
        'vmin' not in kwargs and
        'vmax' not in kwargs):
        kwargs['use_std'] = True

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Measure sigma")

    # Create a Matplotlib figure
    # If I use mpl.pyplot.figure here and this function is used in a
    # notebook, an inline plot of the final figure will be shown.
    fig = mpl.figure.Figure(figsize=(7, 6), dpi=100)
    ax, img = add_wcs_axes(fig, 1, 1, 1, fitsmap=fitsmap, **kwargs)
    cbar = insert_colorbar(ax)

    # Prettier plot
    current_title = ax.get_title()
    ax.set_title(current_title, fontsize=13, pad=15)
    ax.coords[0].set_axislabel("RA (ICRS)", fontsize=12)
    ax.coords[1].set_axislabel("DEC (ICRS)", fontsize=12)
    ax.coords[0].tick_params(which="major",
                            length=5)
    ax.coords[0].display_minor_ticks(True)
    ax.coords[0].set_ticklabel(size=11, exclude_overlapping=True)
    ax.coords[1].tick_params(which="major",
                            length=5)
    ax.coords[1].display_minor_ticks(True)
    ax.coords[1].set_ticklabel(size=11, exclude_overlapping=True,
                               rotation='vertical')
    cbar.ax.yaxis.label.set_fontsize(12)
    cbar.ax.tick_params(labelsize=11)

    # Lists to store the polygons and arrays with pixel data
    polygon_paths = []
    current_polygon = []
    inside_pixels = []
    sigma = np.nan

    # Create a callback function for mouse clicks
    def onclick(event):
        nonlocal polygon_paths, current_polygon
        # Left-click to select points
        if event.button == 1:
            # Add the clicked point to the current polygon
            current_polygon.append((event.xdata, event.ydata))
            now_polygon = np.array(current_polygon)
            # Draw a small point at the first clicked point
            if len(now_polygon) == 1:
                ax.plot(event.xdata, event.ydata,
                        'white', marker='o', markersize=5)
            # Draw lines
            if len(now_polygon) > 1:
                ax.plot(now_polygon[-2:, 0], now_polygon[-2:, 1],
                        'white', lw=2, alpha=0.9)
                ax.plot(event.xdata, event.ydata,
                        'white', marker='o', markersize=5)
            # Refresh the canvas
            canvas.draw()
        # Right-click to finalize the current polygon
        elif event.button == 3 and current_polygon:
            polygon = np.array(current_polygon)
            # Draw the last side of the polygon
            closed_polygon = np.vstack((polygon, polygon[0]))
            ax.plot(closed_polygon[-2:, 0], closed_polygon[-2:, 1],
                    'white', lw=2, alpha=0.9)
            # Draw the polygon on the plot
            poly = patches.Polygon(xy=polygon, linewidth=2,
                                   edgecolor='white', facecolor='white',
                                   alpha=0.5)
            new_poly = copy(poly)
            ax.add_patch(new_poly)
            # Get the shape of the CCDData object
            if fitsmap.header['NAXIS'] == 2:
                height, width = fitsmap.data.shape
                fitsmap_data = fitsmap.data
            elif fitsmap.header['NAXIS'] == 3:
                freq, height, width = fitsmap.data.shape
                fitsmap_data = fitsmap.data[0,:,:]
            elif fitsmap.header['NAXIS'] == 4:
                freq, stokes, height, width = fitsmap.data.shape
                fitsmap_data = fitsmap.data[0,0,:,:]
            # Create a meshgrid of coordinates to create mask
            x, y = np.meshgrid(range(width), range(height))
            points = np.vstack((x.flatten(), y.flatten())).T
            mask = poly.contains_points(points, radius=0)
            mask = mask.reshape((height, width))
            # Calculate std
            new_data = copy(fitsmap_data)
            std = new_data[mask].std(ddof=1)
            # Paint std inside polygon
            x_text = polygon.T[0].min() + (polygon.T[0].max()
                                           - polygon.T[0].min()) / 2
            y_text = polygon.T[1].min() + (polygon.T[1].max() 
                                           - polygon.T[1].min()) / 2
            std_text = ax.text(x_text, y_text, f'{std:.2f}',
                               va='center', ha='center',
                               color='white', fontsize=13)
            std_text.set_path_effects(
                [PathEffects.withStroke(linewidth=1.5, foreground="0.5")]
            )
            # Add info on lists
            polygon_paths.append(polygon)
            inside_pixels.append(new_data[mask])
            # Reset the current polygon
            current_polygon = []
            # Refresh the canvas
            canvas.draw()

    # Close function
    def _quit():
        sigma = get_sigma()
        if not np.isnan(sigma):
            root.quit()
            root.destroy()
        else:
            root.quit()
            root.destroy()

    # Close shortcut
    def onkeypress(event):
        if event.key == 'q':
            _quit()

    # Clear all drawn and selected polygons
    def clear_polygons():
        nonlocal polygon_paths
        nonlocal current_polygon
        nonlocal inside_pixels
        nonlocal sigma
        # Reset sigma lists
        polygon_paths = []
        current_polygon = []
        inside_pixels = []
        sigma = np.nan
        # Remove sigma painted objects
        # Remove lines and scatter points
        for line in ax.lines:
            line.remove()
        # Remove patches
        for patch in ax.patches:
            patch.remove()
        # Remove texts
        for text in ax.texts:
            text.remove()
        canvas.draw()

    # Calculate sigma
    def get_sigma():
        nonlocal sigma
        all_data = np.array([])
        for inside_data in inside_pixels:
            all_data = np.append(all_data, inside_data)
        if statistic == 'std':
            sigma = np.std(all_data, ddof=1)
        elif statistic == 'rms':
            sigma = np.sqrt(np.mean(np.square(all_data)))
        return sigma

    # Change sigma statistic
    def change_to_std():
        nonlocal statistic
        statistic = 'std'
        sigma_button.config(relief=tk.SUNKEN)
        check_button.config(relief=tk.RAISED)
    def change_to_rms():
        nonlocal statistic
        statistic = 'rms'
        sigma_button.config(relief=tk.RAISED)
        check_button.config(relief=tk.SUNKEN)

    # Create a Matplotlib canvas embedded within the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Show toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Create a frame for the statistic buttons
    stat_frame = tk.Frame(root)
    stat_frame.pack(side=tk.TOP, pady=5)
    if statistic == 'std':
        sigma_button = tk.Button(stat_frame, text="STD",
                                relief='sunken', command=change_to_std)
        sigma_button.pack(side=tk.LEFT, padx=3)
        check_button = tk.Button(stat_frame, text="RMS",
                                command=change_to_rms)
        check_button.pack(side=tk.LEFT, padx=3)
    elif statistic == 'rms':
        sigma_button = tk.Button(stat_frame, text="STD",
                                command=change_to_std)
        sigma_button.pack(side=tk.LEFT, padx=3)
        check_button = tk.Button(stat_frame, text="RMS",
                                relief='sunken', command=change_to_rms)
        check_button.pack(side=tk.LEFT, padx=3)

    # Create a frame for main buttons
    sigma_frame = tk.Frame(root)
    sigma_frame.pack(side=tk.BOTTOM)
    clear_button = tk.Button(sigma_frame, text="Clear", command=clear_polygons)
    clear_button.pack(side=tk.LEFT, padx=3)
    abort_button_sigma = tk.Button(sigma_frame, text="Finish", command=_quit)
    abort_button_sigma.pack(side=tk.RIGHT, padx=3)

    # Connect the onclick and onkeypress events to the canvas
    canvas.mpl_connect('button_press_event', onclick)
    canvas.mpl_connect('key_press_event', onkeypress)
    
    # Start the Tkinter event loop
    tk.mainloop()

    return sigma


def get_input(obj, **kwargs):
    """
    Get the pixel coordinates of points selected by mouse clicks in a
    previously plotted figure or a map object.

    Parameters
    ----------
    obj : `~matplotlib.figure.Figure`, \
          `~astropy.nddata.CCDData`, or \
          `~madcubapy.io.MadcubaMap` object.
        Figure or Map object to show and from which to get coordinates.

    Returns
    -------
    selected_points : `numpy.array`
        Coordinates of the clicked points.

    Other Parameters
    ----------------    
    **kwargs
        Optional map visualization parameters passed to
        :func:`~madcubapy.visualization.add_wcs_axes` only if `obj` is a
        `~astropy.nddata.CCDData` or `~madcubapy.io.MadcubaMap` object.
        
    """
    
    if isinstance(obj, plt.Figure):
        return _get_input_from_figure(obj)
    elif isinstance(obj, CCDData) or isinstance(obj, MadcubaMap):
        return _get_input_from_map(obj, **kwargs)
    else:
        raise TypeError("Unsupported type. " +
            "Provide a Matplotlib Figure, MadcubaMap, or CCDData object.")


def _get_input_from_figure(fig):
    """
    Returns mouse click coordinates using a previously created figure.

    Parameters
    ----------
    fig : `~matplotlib.figure.Figure`
        Figure object to show and from which to get coordinates.

    Returns
    -------
    selected_points : `numpy.array`
        Coordinates of the clicked points.

    """
    
    original_backend = mpl.get_backend()

    try:
        # Change matplotlib backend to tkinter
        mpl.use("TkAgg", force=True)  # Switch to TkAgg
        # Bring figure back from the dead
        new_fig = plt.figure()
        new_manager = new_fig.canvas.manager
        new_manager.canvas.figure = fig
        fig.set_canvas(new_manager.canvas)
        # Get input from clicks
        selected_points = fig.ginput(
            n=0, timeout=0, mouse_add=1, mouse_pop=2, mouse_stop=3
        )
        # Close figure to prevent issues
        plt.close('all')
    except Exception as e:
        raise RuntimeError(
            f"Failed to execute operation with TkAgg backend: {e}"
        )
    finally:
        try:
            # Change matplotlib backend back to inline
            mpl.use(original_backend, force=True)  # Restore original backend
            plt.close("all")  # Close any figures to prevent issues
        except Exception as e:
            raise RuntimeError(
                f"Failed to restore original backend ({original_backend}): {e}"
            )

    return np.array(selected_points)


def _get_input_from_map(fitsmap, **kwargs):
    """
    Returns mouse click coordinates using a `~astropy.nddata.CCDData` or
    `~madcubapy.io.madcubaMap` object.

    Parameters
    ----------
    fitsmap : `~astropy.nddata.CCDData` or `~madcubapy.io.MadcubaMap`
        Map object to show and from which to get coordinates.

    Returns
    -------
    selected_points : `numpy.array`
        Coordinates of the clicked points.

    Other Parameters
    ----------------
    **kwargs
        Parameters to pass to :func:`~madcubapy.visualization.add_wcs_axes`.

    """

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Sigma calculation")

    # Create a Matplotlib figure
    fig = mpl.figure.Figure(figsize=(7, 6), dpi=100)
    ax, img = add_wcs_axes(fig, 1, 1, 1, fitsmap=fitsmap, **kwargs)
    cbar = insert_colorbar(ax)

    # Prettier plot
    ax.set_title('Sigma calculation', fontsize=15, pad=20)
    ax.coords[0].set_axislabel("RA (ICRS)", fontsize=12)
    ax.coords[1].set_axislabel("DEC (ICRS)", fontsize=12)
    ax.coords[0].tick_params(which="major",
                            length=5)
    ax.coords[0].display_minor_ticks(True)
    ax.coords[0].set_ticklabel(size=11, exclude_overlapping=True)
    ax.coords[1].tick_params(which="major",
                            length=5)
    ax.coords[1].display_minor_ticks(True)
    ax.coords[1].set_ticklabel(size=11, exclude_overlapping=True,
                               rotation='vertical')
    cbar.ax.yaxis.label.set_fontsize(12)
    cbar.ax.tick_params(labelsize=11)

    # Lists to store selected points and plot markers
    selected_points = []
    plot_markers = []

    # Create a callback function for mouse clicks
    def onclick(event):
        nonlocal selected_points, plot_markers
        # Left-click to select points
        if event.button == 1:
            if event.xdata is not None and event.ydata is not None:
                # Add the clicked point to the current polygon
                selected_points.append((event.xdata, event.ydata))
                # Draw the clicked point and add it to the list
                marker = ax.plot(event.xdata, event.ydata,
                                 'red', marker='+', markersize=6)
                plot_markers.append(marker)
                # Refresh the canvas
                canvas.draw()
        # Middle-click to remove last selected point
        elif event.button == 2:
            if selected_points:
                # Remove last selected point
                selected_points.pop()
                # Remove last painted point from plot and list
                marker = plot_markers[-1][0]
                marker.remove()
                plot_markers.pop()
                # Refresh the canvas
                canvas.draw()
        # Right-click to finalize the current polygon
        elif event.button == 3:
            # Refresh the canvas
            _quit()

    # Function to clear all selected points
    def clear_points():
        nonlocal selected_points, plot_markers
        # Remove all selected points
        selected_points.clear()
        # Remove all painted points
        while plot_markers:
            marker = plot_markers[-1][0]
            marker.remove()
            plot_markers.pop()
        canvas.draw()

    # Exit function to close the window
    def _quit():
        root.quit()
        root.destroy()

    # Add close shortcut
    def onkeypress(event):
        if event.key == 'q':
            root.quit()
            root.destroy()

    # Create a Matplotlib canvas embedded within the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Add matplotlib tk toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Create a frame for buttons
    control_frame = tk.Frame(root)
    control_frame.pack(side=tk.BOTTOM, pady=5)
    # "Clear All" button
    clear_button = tk.Button(control_frame, text="Clear All", command=clear_points)
    clear_button.pack(side=tk.LEFT, padx=5)
    # "Finish" button
    finish_button = tk.Button(control_frame, text="Finish", command=_quit)
    finish_button.pack(side=tk.RIGHT, padx=5)

    # Connect the onclick and onkeypress events to the canvas
    canvas.mpl_connect('button_press_event', onclick)
    canvas.mpl_connect('key_press_event', onkeypress)
    
    # Start the Tkinter event loop
    root.mainloop()

    return np.array(selected_points)
