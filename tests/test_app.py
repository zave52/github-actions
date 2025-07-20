import pytest

from myapp.app import add, subtract


@pytest.mark.parametrize(
    "num1,num2,result",
    [
        (10, 20, 30),
        (10, -100, -90),
        (0, 0, 0),
        (45.1, 19.7, 64.8),
        (0.1, -0.1, 0)
    ]
)
def test_add(num1: int | float, num2: int | float, result: int | float) -> None:
    assert add(num1, num2) == result


@pytest.mark.parametrize(
    "num1,num2,result",
    [
        (10, 20, -10),
        (10, -100, 110),
        (0, 0, 0),
        (45.1, 19.7, 25.4),
        (0.1, -0.1, 0.2)
    ]
)
def test_subtract(
    num1: int | float,
    num2: int | float,
    result: int | float
) -> None:
    assert subtract(num1, num2) == result
