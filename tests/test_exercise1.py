import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even_returns_true_for_even_numbers():
    """Test that is_even returns True for even numbers like 4."""
    assert is_even(4) == True


# bug report 2
def test_r2_rectangle_area_returns_product():
    """Test that rectangle_area returns the product of width and height, not their sum."""
    assert rectangle_area(5, 3) == 15


# bug report 3
def test_r3_double_returns_twice_the_number():
    """Test that double(n) returns twice the number n as stated in the docstring."""
    assert double(5) == 10
