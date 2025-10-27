# test_app.py
import pytest
from app import add, multiply, greet

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("") == "Hello, !"