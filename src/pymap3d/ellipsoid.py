"""Minimal class for planetary ellipsoids"""
from math import sqrt


class Ellipsoid:
    """
    generate reference ellipsoid parameters

    as everywhere else in this program, distance units are METERS

    Ellipsoid sources
    -----------------

    maupertuis, plessis, everest1830, everest1830m, everest1967,
    airy, bessel, clarke1866, clarke1878, clarke1860, helmert, hayford,
    international1924, krassovsky1940, wgs66, australian, international1967,
    grs67, sa1969, wgs72, iers1989, iers2003:

    - https://en.wikipedia.org/wiki/Earth_ellipsoid#Historical_Earth_ellipsoids
    - https://en.wikibooks.org/wiki/PROJ.4#Spheroid

    wgs84: https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84

    grs80: https://en.wikipedia.org/wiki/GRS_80

    io: https://doi.org/10.1006/icar.1998.5987

    pz90.11: https://structure.mil.ru/files/pz-90.pdf

    gsk2011: https://racurs.ru/downloads/documentation/gost_r_32453-2017.pdf

    mars: https://tharsis.gsfc.nasa.gov/geodesy.html

    mercury, venus, moon, jupiter, saturn, uranus, neptune:

    - https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html

    feel free to suggest additional ellipsoids
    """

    def __init__(self, model: str = "wgs84"):
        """
        feel free to suggest additional ellipsoids

        Parameters
        ----------
        model : str
                name of ellipsoid
        """

        models = {
            # Earth ellipsoids
            'maupertuis': {'name': 'Maupertuis (1738)', 'a': 6397300.0, 'b': 6363806.283},
            'plessis': {'name': 'Plessis (1817)', 'a': 6376523.0, 'b': 6355862.9333},
            'everest1830': {'name': 'Everest (1830)', 'a': 6377299.365, 'b': 6356098.359},
            'everest1830m': {'name': 'Everest 1830 Modified (1967)', 'a': 6377304.063, 'b': 6356103.039},
            'everest1967': {'name': 'Everest 1830 (1967 Definition)', 'a': 6377298.556, 'b': 6356097.55},
            'airy': {'name': 'Airy (1830)', 'a': 6377563.396, 'b': 6356256.909},
            'bessel': {'name': 'Bessel (1841)', 'a': 6377397.155, 'b': 6356078.963},
            'clarke1866': {'name': 'Clarke (1866)', 'a': 6378206.4, 'b': 6356583.8},
            'clarke1878': {'name': 'Clarke (1878)', 'a': 6378190.0, 'b': 6356456.0},
            'clarke1860': {'name': 'Clarke (1880)', 'a': 6378249.145, 'b': 6356514.87},
            'helmert': {'name': 'Helmert (1906)', 'a': 6378200.0, 'b': 6356818.17},
            'hayford': {'name': 'Hayford (1910)', 'a': 6378388.0, 'b': 6356911.946},
            'international1924': {'name': 'International (1924)', 'a': 6378388.0, 'b': 6356911.946},
            'krassovsky1940': {'name': 'Krassovsky (1940)', 'a': 6378245.0, 'b': 6356863.019},
            'wgs66': {'name': 'WGS66 (1966)', 'a': 6378145.0, 'b': 6356759.769},
            'australian': {'name': 'Australian National (1966)', 'a': 6378160.0, 'b': 6356774.719},
            'international1967': {'name': 'New International (1967)', 'a': 6378157.5, 'b': 6356772.2},
            'grs67': {'name': 'GRS-67 (1967)', 'a': 6378160.0, 'b': 6356774.516},
            'sa1969': {'name': 'South American (1969)', 'a': 6378160.0, 'b': 6356774.719},
            'wgs72': {'name': 'WGS-72 (1972)', 'a': 6378135.0, 'b': 6356750.52001609},
            'grs80': {'name': 'GRS-80 (1979)', 'a': 6378137.0, 'b': 6356752.31414036},
            'wgs84': {'name': 'WGS-84 (1984)', 'a': 6378137.0, 'b': 6356752.31424518},
            'iers1989': {'name': 'IERS (1989)', 'a': 6378136.0, 'b': 6356751.302},
            "pz90.11": {'name': 'ПЗ-90 (2011)', 'a': 6378136.0, 'b': 6356751.3618},
            'iers2003': {'name': 'IERS (2003)', 'a': 6378136.6, 'b': 6356751.9},
            "gsk2011": {'name': 'ГСК (2011)', 'a': 6378136.5, 'b': 6356751.758},
            # Other planets
            "mercury": {'name': 'Mercury', 'a': 2440500.0, 'b': 2438300.0},
            "venus": {"name": "Venus", "a": 6051800.0, "b": 6051800.0},
            "moon": {"name": "Moon", "a": 1738100.0, "b": 1736000.0},
            "mars": {"name": "Mars", "a": 3396900.0, "b": 3376097.80585952},
            "jupyter": {"name": "Jupiter", "a": 71492000.0, "b": 66770054.3475922},
            "io": {"name": "Io", "a": 1829.7, "b": 1815.8},
            "saturn": {"name": "Saturn", "a": 60268000.0, "b": 54364301.5271271},
            "uranus": {"name": "Uranus", "a": 25559000.0, "b": 24973000.0},
            "neptune": {"name": "Neptune", "a": 24764000.0, "b": 24341000.0},
            "pluto": {"name": "Pluto", "a": 1188000.0, "b": 1188000.0},
        }

        if model not in models:
            raise NotImplementedError(
                f"{model} model not implemented, let us know and we will add it (or make a pull request)"
            )

        self.model = model                 # short name
        self.name = models[model]["name"]  # name for printing
        self.semimajor_axis = models[model]['a']
        self.semiminor_axis = models[model]['b']
        self.flattening = (self.semimajor_axis - self.semiminor_axis) / self.semimajor_axis
        self.thirdflattening = (self.semimajor_axis - self.semiminor_axis) / (
            self.semimajor_axis + self.semiminor_axis
        )
        self.eccentricity = sqrt(2 * self.flattening - self.flattening**2)
