# test_pairs_of_integers.py
from pairs_of_integers import generate_pairs

def test_generate_pairs_0():
    assert generate_pairs(0) == [[0, 0]]

def test_generate_pairs_2():
    expected = [
        [0, 0], [0, 1], [0, 2],
        [1, 1], [1, 2],
        [2, 2]
    ]
    assert generate_pairs(2) == expected

def test_values_are_in_range():
    n = 5
    result = generate_pairs(n)
    for a, b in result:
        assert 0 <= a <= b <= n
