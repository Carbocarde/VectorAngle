from numba import njit
import numpy as np

from Util import normalize


@njit
def dot_product_norm(v1: np.array, v2: np.array) -> float:
    """
    Calculate the angle two vectors form, using the dot product.

    A*B = |A|*|B|*cos(theta)
    Using unit vectors:
    A*B = 1*1*cos(theta)
    theta = cos^-1(A*B)

    :param v1: Vector 1
    :param v2: Vector 2
    :return: The angle formed by the two vectors
    """
    v1_u = normalize(v1)
    v2_u = normalize(v2)
    rad = np.arccos(np.dot(v1_u, v2_u))
    return np.rad2deg(rad)


@njit
def dot_product_mag(v1: np.array, v2: np.array) -> float:
    """
    Calculate the angle two vectors form, using the dot product.

    A*B = |A|*|B|*cos(theta)
    Using magnitude:
    theta = cos^-1((A*B)/(|A||B|))

    :param v1: Vector 1
    :param v2: Vector 2
    :return: The angle formed by the two vectors
    """
    dot = np.dot(v1, v2)
    v1_mag = np.sqrt(np.dot(v1, v1))
    v2_mag = np.sqrt(np.dot(v2, v2))
    rad = np.arccos(dot / (v1_mag * v2_mag))
    return np.rad2deg(rad)


@njit
def projection(v1: np.array, v2: np.array) -> float:
    """
    Calculate the angle two vectors form, using projection.

    1. project v2 onto v1
           ____
          |   /
      v2  |  / v2
    (proj)| /
          |/
    2. calculate the magnitudes squared of proj and v2
    3. get the angle of the two vertices by calculating cos^-1 of sqrt((mag proj^2)/(mag v2^2))
    4. calculate the dot product of v1 and v2. This will tell us if the angle is less than or greater than 90.

    :param v1: Vector 1
    :param v2: Vector 2
    :return: The angle formed by the two vectors
    """
    # 1 - a*b / (b_mag) * b
    dot = np.dot(v1, v2)
    div = np.dot(v1, v1)
    scalar = dot / div
    projected = scalar * v1
    # 2
    hor_mag_sq = np.sum(projected ** 2)
    hyp_mag_sq = np.sum(v2 ** 2)
    # 3
    # arccos of proj over v2
    rad = np.arccos(np.sqrt(hor_mag_sq / hyp_mag_sq))
    deg = np.rad2deg(rad)
    # 4
    if dot < 0:
        deg = 180 - deg

    return deg
