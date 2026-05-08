from etl import process_claim
import pytest


def test_valid_claim():
    assert process_claim(1000) == 900


def test_invalid_claim():
    with pytest.raises(ValueError):
        process_claim(-100)