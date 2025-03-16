import astropy.units as u
import numpy as np

__all__ = [
    'get_angle_offset_point',
    'get_angle_separation',
    'get_physical_offset_point',
    'get_physical_separation',
]

def get_angle_offset_point(points, ref_point, fitsmap):
    """Get offset coordinates of a point or set of points, with respect to a
    reference point in angular units.

    Parameters
    ----------
    points : `~numpy.ndarray`
        Input point or points.
    ref_point : `~numpy.ndarray`
        Reference point.
    fitsmap : `~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`
        Map from which to get angular size of each pixel (CDELT1, CDELT2).

    Returns
    -------
    points_offset_angle : `~astropy.units.Quantity`
        Points with converted units to angular offset.

    """

    cdelt_deg = fitsmap.wcs.wcs.cdelt[:2] * u.deg
    points_offset_angle = (points - ref_point) * cdelt_deg

    return points_offset_angle


def get_angle_separation(points, ref_point, fitsmap):
    """Get separation between a point or set of points, and a reference pixel
    in angular units.

    Parameters
    ----------
    points : `~numpy.ndarray`
        Input point or points.
    ref_point : `~numpy.ndarray`
        Reference point.
    fitsmap : `~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`
        Map from which to get angular size of each pixel (CDELT1, CDELT2).

    Returns
    -------
    angle_separation : `~astropy.units.Quantity`
        Separation between input points and reference point.

    """

    points_offset_angle = get_angle_offset_point(points, ref_point, fitsmap)
    angle_separation = np.linalg.norm(points_offset_angle, axis=-1)

    return angle_separation


def get_physical_offset_point(points, ref_point, fitsmap, distance):
    """Get offset coordinates of a point or set of points, with respect to a
    reference point in physical distance units.

    Parameters
    ----------
    points : `~numpy.ndarray`
        Input point or points.
    ref_point : `~numpy.ndarray`
        Reference point.
    fitsmap : `~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`
        Map from which to get angular size of each pixel (CDELT1, CDELT2).
    distance : `~astropy.units.quantity`
        Distance from earth to object.

    Returns
    -------
    points_offset_physical : `~astropy.units.Quantity`
        Points with converted units to physical distance offset.

    """

    points_offset_angle = get_angle_offset_point(points, ref_point, fitsmap)

    points_offset_physical = (points_offset_angle * distance).to(
        u.au, equivalencies=u.dimensionless_angles()
    )

    return points_offset_physical


def get_physical_separation(points, ref_point, fitsmap, distance):
    """Get separation between a point or set of points, and a reference pixel
    in physical distance units.

    Parameters
    ----------
    points : `~numpy.ndarray`
        Input point or points.
    ref_point : `~numpy.ndarray`
        Reference point.
    fitsmap : `~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`
        Map from which to get angular size of each pixel (CDELT1, CDELT2).
    distance : `~astropy.units.quantity`
        Distance from earth to object.

    Returns
    -------
    physical_separation : `~astropy.units.Quantity`
        Separation between input points and reference point.

    """

    points_offset_physical = get_physical_offset_point(points, ref_point, fitsmap, distance)
    physical_separation = np.linalg.norm(points_offset_physical, axis=-1)

    return physical_separation
