import pytest

import Angle
import SpecialCases
from Util import random_vector, random_vector_array

VECTOR_COUNT = 100000
NORMALIZE = (False, False)  # Normalize first and/or second vector

test_functions = [Angle.dot_product_norm, Angle.dot_product_mag, Angle.projection]

if NORMALIZE == (True, True):
    test_functions.append(SpecialCases.dot_product_2_unit)
    test_functions.append(SpecialCases.projection_2_unit)
elif NORMALIZE == (True, False):
    test_functions.append(SpecialCases.dot_product_1_unit)
    test_functions.append(SpecialCases.projection_1_unit)


@pytest.fixture(params=test_functions)
def function(request):
    return request.param


# Generate test vectors
test_rand_vectors = [(2, random_vector_array(count=VECTOR_COUNT, dim=2, normalize_elem=NORMALIZE)),
                     (3, random_vector_array(count=VECTOR_COUNT, dim=3, normalize_elem=NORMALIZE)),
                     (4, random_vector_array(count=VECTOR_COUNT, dim=4, normalize_elem=NORMALIZE)),
                     (5, random_vector_array(count=VECTOR_COUNT, dim=5, normalize_elem=NORMALIZE)),
                     (10, random_vector_array(count=VECTOR_COUNT, dim=10, normalize_elem=NORMALIZE)),
                     (20, random_vector_array(count=VECTOR_COUNT, dim=20, normalize_elem=NORMALIZE)),
                     (30, random_vector_array(count=VECTOR_COUNT, dim=30, normalize_elem=NORMALIZE)),
                     (40, random_vector_array(count=VECTOR_COUNT, dim=40, normalize_elem=NORMALIZE)),
                     (50, random_vector_array(count=VECTOR_COUNT, dim=50, normalize_elem=NORMALIZE)),
                     (100, random_vector_array(count=VECTOR_COUNT, dim=100, normalize_elem=NORMALIZE)),]

# Call functions once to ensure they are compiled prior to benchmarking
_ = [x(random_vector(), random_vector()) for x in test_functions]


def vector_set_id(val: tuple):
    return "dim-" + str(val[0])


@pytest.fixture(params=test_rand_vectors, ids=vector_set_id)
def vector_set(request):
    return request.param[1]


@pytest.mark.serial
def test_angle_rand(vector_set, function):
    for angle, v1, v2 in vector_set:
        _ = function(v1, v2)

    assert True
