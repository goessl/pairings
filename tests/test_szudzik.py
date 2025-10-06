from pairings.szudzik import *



def test_pair():
    assert pair(0, 0) == 0
    assert pair(0, 1) == 1
    assert pair(1, 0) == 2
    assert pair(1, 1) == 3
    assert pair(0, 2) == 4
    assert pair(1, 2) == 5
    assert pair(2, 0) == 6
    assert pair(2, 1) == 7
    assert pair(2, 2) == 8
    assert pair(0, 3) == 9
    assert pair(1, 3) == 10
    assert pair(2, 3) == 11
    assert pair(3, 0) == 12
    assert pair(3, 1) == 13
    assert pair(3, 2) == 14
    assert pair(3, 3) == 15

def test_depair():
    assert depair(0) == (0, 0)
    assert depair(1) == (0, 1)
    assert depair(2) == (1, 0)
    assert depair(3) == (1, 1)
    assert depair(4) == (0, 2)
    assert depair(5) == (1, 2)
    assert depair(6) == (2, 0)
    assert depair(7) == (2, 1)
    assert depair(8) == (2, 2)
    assert depair(9) == (0, 3)
    assert depair(10) == (1, 3)
    assert depair(11) == (2, 3)
    assert depair(12) == (3, 0)
    assert depair(13) == (3, 1)
    assert depair(14) == (3, 2)
    assert depair(15) == (3, 3)

def test_pair_and_unpair():
    for n in range(100):
        assert pair(*depair(n)) == n
