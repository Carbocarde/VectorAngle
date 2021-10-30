from numba import njit
import numpy as np

from Util import normalize


@njit
def dot_product_1_unit(v1_u: np.array, v2: np.array) -> float:
    v2_u = normalize(v2)
    rad = np.arccos(np.dot(v1_u, v2_u))
    return np.rad2deg(rad)


@njit
def dot_product_2_unit(v1_u: np.array, v2_u: np.array) -> float:
    rad = np.arccos(np.dot(v1_u, v2_u))
    return np.rad2deg(rad)


@njit
def projection_1_unit(v1_u: np.array, v2: np.array) -> float:
    dot = np.dot(v1_u, v2)
    scalar = dot
    projected = scalar * v1_u

    hor_mag_sq = np.sum(projected ** 2)
    hyp_mag_sq = np.sum(v2 ** 2)

    rad = np.arccos(np.sqrt(hor_mag_sq / hyp_mag_sq))
    deg = np.rad2deg(rad)

    if dot < 0:
        deg = 180 - deg

    return deg


@njit
def projection_2_unit(v1_u: np.array, v2_u: np.array) -> float:
    dot = np.dot(v1_u, v2_u)
    scalar = dot
    projected = scalar * v1_u

    hor_mag_sq = np.sum(projected ** 2)

    rad = np.arccos(np.sqrt(hor_mag_sq))
    deg = np.rad2deg(rad)

    if dot < 0:
        deg = 180 - deg

    return deg
