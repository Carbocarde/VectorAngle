"""
Tests the correctness of each function, in relation to the truth function (what we know to be correct).

Uses pytest fixtures to run every possible combination of function/vector
"""
import numpy as np
import pytest
from math import isclose

import Angle
import SpecialCases
from Util import random_vector_pair, random_vector_array

truth_function = Angle.dot_product_norm
test_functions = [Angle.dot_product_norm, Angle.dot_product_mag, Angle.projection]


@pytest.fixture(params=test_functions)
def function(request):
    return request.param


test_2d_vectors = [
    ("45_", [0, 1], [1, 1]),
    ("45_", [1, 1], [1, 0]),
    ("45_", [-1, -1], [-1, 0]),
    ("90_", [0, 1], [1, 0]),
    ("90_", [0, -1], [-1, 0]),
]

test_3d_vectors = [
    ("45_", [0, 1, 0], [0, 1, 1]),
    ("45_", [1, 1, 0], [1, 0, 0]),
    ("90_", [0, 1, 0], [1, 0, 0]),
    ("90_", [0, 0, 1], [0, 1, 0]),
    ("135_", [0, -1, 1], [0, 1, 0]),
    ("rand", [734, -537, 52], [653, 215, 85])
]

test_nd_vectors = [
    ("00", [0, 1, 0, 0], [0, 1, 0, 0]),
    ("45_", [0, 1, 0, 0], [0, 1, 1, 0]),
    ("45_", [1, 1, 0, 0], [1, 0, 0, 0]),
    ("90_", [0, 1, 0, 0], [1, 0, 0, 0]),
    ("90_", [0, 0, 1, 0], [0, 0, 0, 1]),
    ("135", [0, 1, 0, 0], [1, -1, 0, 0]),
    ("180", [0, 1, 0, 0], [0, -1, 0, 0]),
    ("rand", [5098, 214, -323, -123], [-321, 76, 45, 72]),
]


def idfn(val: tuple):
    """Extracts vector name from named testcases"""
    return val[0]


@pytest.fixture(params=test_2d_vectors, ids=idfn)
def vector_2d(request):
    angle, v1, v2 = request.param

    v1 = np.array(v1, dtype="float64")
    v2 = np.array(v2, dtype="float64")

    return angle, v1, v2


@pytest.fixture(params=test_3d_vectors, ids=idfn)
def vector_3d(request):
    angle, v1, v2 = request.param

    v1 = np.array(v1, dtype="float64")
    v2 = np.array(v2, dtype="float64")

    return angle, v1, v2


@pytest.fixture(params=test_nd_vectors, ids=idfn)
def vector_nd(request):
    angle, v1, v2 = request.param

    v1 = np.array(v1, dtype="float64")
    v2 = np.array(v2, dtype="float64")

    return angle, v1, v2


def test_2d_angle(function, vector_2d):
    angle, v1, v2 = vector_2d

    assert isclose(function(v1, v2), truth_function(v1, v2), abs_tol=0.00001)


def test_3d_angle(function, vector_3d):
    angle, v1, v2 = vector_3d

    assert isclose(function(v1, v2), truth_function(v1, v2), abs_tol=0.00001)


def test_nd_angle(function, vector_nd):
    angle, v1, v2 = vector_nd

    assert isclose(function(v1, v2), truth_function(v1, v2), abs_tol=0.00001)


# Random vector brute testing
test_nd_rand_vectors = [random_vector_pair(seed=i) for i in range(100)]
test_2d_rand_vectors = random_vector_array(dim=2, count=100)
test_3d_rand_vectors = random_vector_array(dim=3, count=100)


@pytest.fixture(params=test_2d_rand_vectors)
def vector_2d_rand(request):
    angle, v1, v2 = request.param

    return angle, v1, v2


@pytest.fixture(params=test_3d_rand_vectors)
def vector_3d_rand(request):
    angle, v1, v2 = request.param

    return angle, v1, v2


@pytest.fixture(params=test_nd_rand_vectors)
def vector_nd_rand(request):
    angle, v1, v2 = request.param

    return angle, v1, v2


def test_2d_angle_rand(function, vector_2d_rand):
    angle, v1, v2 = vector_2d_rand

    assert isclose(function(v1, v2), truth_function(v1, v2), abs_tol=0.00001)


def test_3d_angle_rand(function, vector_3d_rand):
    angle, v1, v2 = vector_3d_rand

    assert isclose(function(v1, v2), truth_function(v1, v2), abs_tol=0.00001)


def test_nd_angle_rand(function, vector_nd_rand):
    angle, v1, v2 = vector_nd_rand

    assert isclose(function(v1, v2), truth_function(v1, v2), abs_tol=0.00001)


# Testing Special Cases
test_1_unit_functions = test_functions + [SpecialCases.dot_product_1_unit, SpecialCases.projection_1_unit]
test_2_unit_functions = test_functions + [SpecialCases.dot_product_2_unit, SpecialCases.projection_2_unit]


@pytest.fixture(params=test_1_unit_functions)
def function_1_unit(request):
    return request.param


@pytest.fixture(params=test_2_unit_functions)
def function_2_unit(request):
    return request.param


# Brute Testing Special Cases
test_nd_rand_vectors_1_unit = [random_vector_pair(normalize_elem=(True, False), min_dim=2, max_dim=100, seed=i) for i in range(100)]
test_nd_rand_vectors_2_unit = [random_vector_pair(normalize_elem=(True, True), min_dim=2, max_dim=100, seed=i) for i in range(100)]


@pytest.fixture(params=test_nd_rand_vectors_1_unit)
def vector_nd_rand_1_unit(request):
    angle, v1, v2 = request.param

    return angle, v1, v2


@pytest.fixture(params=test_nd_rand_vectors_2_unit)
def vector_nd_rand_2_unit(request):
    angle, v1, v2 = request.param

    return angle, v1, v2


def test_nd_angle_rand_1_unit(function_1_unit, vector_nd_rand_1_unit):
    angle, v1, v2 = vector_nd_rand_1_unit

    assert isclose(function_1_unit(v1, v2), truth_function(v1, v2), abs_tol=0.00001)


def test_nd_angle_rand_2_unit(function_2_unit, vector_nd_rand_2_unit):
    angle, v1, v2 = vector_nd_rand_2_unit

    assert isclose(function_2_unit(v1, v2), truth_function(v1, v2), abs_tol=0.00001)