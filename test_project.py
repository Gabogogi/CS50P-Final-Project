from project import check_weight
from project import cost_calculator
from project import expected_time
import pytest


def test_check_weight():
    assert check_weight(100) == 100.0
    assert check_weight(50) == 50.0
    assert check_weight(0) is None
    assert check_weight(150) is None
    assert check_weight("abc") is None
    assert check_weight(None) is None

def test_cost_calculator():
    assert cost_calculator(5, 50) == 250.0
    assert cost_calculator(3.5, 30) == 105
    assert cost_calculator(0, 0) == 0

def test_expected_time():
    assert expected_time(120) == (2, 0)
    assert expected_time(90.5) == (1, 30)
    with pytest.raises(ValueError, match="Distance should be a non-negative number"):
        expected_time(-50)

    with pytest.raises(ValueError, match="Distance should be a non-negative number"):
        expected_time("abc")