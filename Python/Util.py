import random
import numpy as np
from numba import njit


@njit
def normalize(v: np.array) -> np.array:
    """
    Return the given vector scaled to length 1.

    :param v: Vector to Normalize
    :return: Normalized Vector
    """
    return v / np.linalg.norm(v)


@njit
def random_vector_array(count=100, dim=100, normalize_elem=(False, False)) -> list:
    """
    Generates a list of vector pairs with the specified attributes.

    :param count: Number of vector pairs to generate
    :param dim: Dimension of the generated vector pairs
    :param normalize_elem: Which vectors in the pairs should be normalized
    :return: List of vector pairs
    """
    arr = []
    for i in range(count):
        arr.append(random_vector_pair(min_dim=dim, max_dim=dim, seed=i, normalize_elem=normalize_elem))
    return arr


@njit
def random_vector_pair(min_dim=1, max_dim=100, normalize_elem=(False, False), seed=random.random()):
    """
    Generates a vector pair with the given attributes.

    :param min_dim: Minimum dimension of generated vector
    :param max_dim: Maximum dimension of generated vector
    :param normalize_elem: Which vectors to normalize after generating
    :param seed: Seed for random. Allows for repeated testing.
    :return: Vector pair with the given attributes
    """
    random.seed(seed)
    seed2 = random.randint(-1000, -1)

    dim = random.randint(min_dim, max_dim)

    v1 = random_vector(dimension=dim, normalize_elem=normalize_elem[0], seed=seed)
    v2 = random_vector(dimension=dim, normalize_elem=normalize_elem[1], seed=seed2)

    return "rand", v1, v2


@njit
def random_vector(dimension=2, normalize_elem=False, max=10000, min=-100000, seed=random.random()):
    """
    Generates a vector with the given attributes.

    :param dimension: Dimension of vector to generate
    :param normalize_elem: Should we normalize this vector before returning it?
    :param max: Max value of generated vector component
    :param max: Min value of generated vector component
    :param seed: Seed for random. Allows for repeated testing.
    :return: Vector with given attributes
    """
    np.random.seed(seed)
    vector = [np.random.uniform(max, min) for _ in range(dimension)]

    vector = np.array(vector, dtype="float64")

    if normalize_elem:
        vector = normalize(vector)

    return vector
