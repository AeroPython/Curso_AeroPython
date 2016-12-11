import numpy as np
from astropy.coordinates import angles


k_Sun = 132749351440.0


def rv2coe(k, a, ecc, inc, raan, argp, nu):
    """Convierte elementos keplerianos a vectores r y v.

    Parámetros
    ==========
    k : float
        Parámetro gravitacional (km^3 / s^2)
    a : float
        Semieje mayor (km)
    ecc : float
        Excentricidad
    inc : float
        Inclinación (rad)
    raan : float
        Ascensión recta del nodo ascendente (rad)
    argp : float
        Argumento del perigeo (rad)
    nu : float
        Anomalía verdadera (rad)

    Devuelve
    ========
    r, v : arrays
        Vectores posición (km) y velocidad (km / s)

    """
    p = a * (1 - ecc ** 2)
    r_pqw = p * np.array([np.cos(nu) / (1 + ecc * np.cos(nu)),
                          np.sin(nu) / (1 + ecc * np.cos(nu)),
                          0])
    v_pqw = np.sqrt(k / p) * np.array([-np.sin(nu),
                                       ecc + np.cos(nu),
                                       0])
    r_ijk = transform(r_pqw, -argp, 'z')
    r_ijk = transform(r_ijk, -inc, 'x')
    r_ijk = transform(r_ijk, -raan, 'z')
    v_ijk = transform(v_pqw, -argp, 'z')
    v_ijk = transform(v_ijk, -inc, 'x')
    v_ijk = transform(v_ijk, -raan, 'z')
    return r_ijk, v_ijk


def rotate(vec, angle, axis):
    """Rotates the coordinate system around axis 1, 2 or 3 a CCW angle.

    Parameters
    ----------
    vec : array
        Dimension 3 vector.
    ax : int
        Axis to be rotated.
    angle : float
        Angle of rotation (rad).
    
    """
    assert vec.shape == (3,)
    rot = np.eye(3)
    if axis == 'x':
        sl = slice(1, 3)
    elif axis == 'y':
        sl = slice(0, 3, 2)
    elif axis == 'z':
        sl = slice(0, 2)
    rot[sl, sl] = np.array([
        [np.cos(angle), np.sin(angle)],
        [-np.sin(angle), np.cos(angle)]
    ])
    return np.dot(rot, vec)


def transform(vector, angle, axis):
    """Rotates a coordinate system around axis a positive right-handed angle.

    Notes
    -----
    This is a convenience function, equivalent to
    `rotate(vec, -angle, axis, unit)`.
    Refer to the documentation of that function for further information.

    """
    return rotate(vector, -angle, axis)