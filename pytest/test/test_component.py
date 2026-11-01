#No need of ../component as pytest automatically adds project's root directory to Python's path when you run it
from component import add, divide 
import pytest

def test_add():
    assert add(2, 3) == 5, "2 plus 3 is equal to 5"

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by 0"):
        divide(6, 0) 
    assert divide(6, 3) == 2, "6 divided by 3 is equal to 2"    