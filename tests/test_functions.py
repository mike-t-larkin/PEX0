import random

from pytest import approx

import arithmetic


def test_add():
    assert arithmetic.add(1, 1) == 2
    assert arithmetic.add(2, 0.5) == 2.5
    assert arithmetic.add(0, -1) == -1

    x = random.random()
    y = random.random()
    assert arithmetic.add(x, y) == approx(x + y)


def test_subtract():
    assert arithmetic.subtract(1, 1) == 0
    assert arithmetic.subtract(2, 0.5) == 1.5
    assert arithmetic.subtract(0, -1) == 1

    x = random.random()
    y = random.random()
    assert arithmetic.subtract(x, y) == approx(x - y)


def test_multiply():
    assert arithmetic.multiply(1, 1) == 1
    assert arithmetic.multiply(2, 0.5) == 1
    assert arithmetic.multiply(0, -1) == 0

    x = random.random()
    y = random.random()
    assert arithmetic.multiply(x, y) == approx(x * y)


def test_divide():
    assert arithmetic.divide(1, 1) == 1
    assert arithmetic.divide(2, 0.5) == 4
    assert arithmetic.divide(0, -1) == 0

    x = random.random()
    y = random.random()
    assert arithmetic.divide(x, y) == approx(x / y)
