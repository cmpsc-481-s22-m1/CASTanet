"""This module test the counter.py module regarding if statements"""
import pytest
from castanet import counter

@pytest.mark.parametrize(
    "string", "expected",
    [
        ("", "")
    ]
)

def test_identifing_ifs():
    """Check that match_ifstatements identifies all of the if-statements in a directory"""
