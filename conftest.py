import pytest
from calculator import Calculator


@pytest.fixture(scope="module")
def calculator():
    return Calculator()
