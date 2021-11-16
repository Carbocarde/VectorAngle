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
    v1_mag = np.dot(v1, v1)
    v2_mag = np.dot(v2, v2)
    rad = np.arccos(dot / np.sqrt(v1_mag * v2_mag))
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


def change_of_basis(v1: np.array, v2: np.array) -> float:
    """
    The intuition behind this is to find a linear transform that transforms v1 and v2 into a new basis space where v1
    is a basis vector.

    This is Passive Transformation.
    https://en.wikipedia.org/wiki/Active_and_passive_transformation

    :param v1: Vector 1
    :param v2: Vector 2
    :return: The angle formed by the two vectors
    """
    angle = 0

    return angle


def rotation(v1: np.array, v2: np.array) -> float:
    """
    The intuition behind this is to find a linear transform that rotates v1 into a single component (along an existing basis vector).

    This is Active Transformation.
    https://en.wikipedia.org/wiki/Active_and_passive_transformation

    :param v1: Vector 1
    :param v2: Vector 2
    :return: The angle formed by the two vectors
    """
    angle = 0

    return angle


def component_angles(v1: np.array, v2: np.array) -> float:
    """
    The intuition behind this is to calculate the angles of each of the components of the vector relative to the basis vectors.
    Then use those individual measurements to find the angle between both vectors.

    :param v1: Vector 1
    :param v2: Vector 2
    :return: The angle formed by the two vectors
    """
    angle = 0

    return angle


@njit
def dot_bin_search(v1: np.array, v2: np.array, accuracy=0.000001) -> float:
    """
    Using binary search, compare the current angle guess with the actual and refine the guess.

    Basic method that just shows that we can generate the angle by seeing if the guess is in front of/behind the actual.

    :param v1: Vector 1
    :param v2: Vector 2
    :param accuracy: The accuracy needed for the output (higher number means faster)
    :return: The angle between two vectors, with up to accuracy size error
    """
    angle = 90
    delta = 45

    dot_angle = dot_product_mag(v1, v2)

    while delta > accuracy:
        if dot_angle > angle:
            angle += delta
        else:
            angle -= delta

        delta /= 2

    return angle


@njit
def proj_bin_search(v1: np.array, v2: np.array, accuracy=0.000001) -> float:
    """
    Calculate the angle two vectors form, using projection and binary search.

    This method uses projection to generate a vector perpendicular to v2, if the angle is equal to the guess.

    1. project v2 onto v1
                ____
       v2(proj)|  / v2
               | /
               |/
    2. Scale (v2 - proj) vector according to the angle guess to form 90 deg threshold
        - The goal is to create a 90 degree angle between v2 & v3 iff v2 & v1 already form the exact given angle

        v3_____|____v2
          \    |  /
            \  | /
              \|/

    3. Update Guess using v1 dot v3
    4. Repeat steps 2 and 3 until the accuracy is within the specified bounds.

    :param v1: Vector 1
    :param v2: Vector 2
    :param accuracy: Max difference from the actual vector angle and the reported
    :return: The angle formed by the two vectors
    """
    # 1
    dot = np.dot(v1, v2)
    div = np.dot(v1, v1)
    scalar = dot / div
    proj = scalar * v1

    diff = proj - v2

    angle = 90
    delta = 45

    # Initialize angle beyond initial 90 degree guess
    if dot < 0:
        angle += delta
    else:
        angle -= delta

    delta /= 2

    while delta > accuracy:
        # Convert angles >90 to be less than 90 for the sake of calculations
        gt = False
        ratio_angle = angle
        if angle > 90:
            gt = True
            ratio_angle = 180 - ratio_angle

        # Scale diff according to angle
        # Ratio between the diff vector and residual vector
        #  - Note: v3 = diff + residual
        # tan(theta) / tan(pi/2 - theta)
        ratio = np.power(np.tan(np.deg2rad(ratio_angle)), 2)
        residual = diff / ratio
        v3 = proj + residual

        dot = np.dot(v2, v3)

        if gt:
            dot = -dot

        if dot > 0:
            angle -= delta
        else:
            angle += delta

        delta /= 2

    return angle
