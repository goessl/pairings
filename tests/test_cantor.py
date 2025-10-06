from itertools import islice
from pairings.cantor import *



def test_pair():
    #1D
    for i in range(20):
        assert pair(i) == i
    #2D
    assert pair(0, 0) == 0
    assert pair(1, 0) == 1
    assert pair(0, 1) == 2
    assert pair(2, 0) == 3
    assert pair(1, 1) == 4
    assert pair(0, 2) == 5
    assert pair(3, 0) == 6
    assert pair(2, 1) == 7
    assert pair(1, 2) == 8
    assert pair(0, 3) == 9
    #3D
    assert pair(0, 0, 0) == 0
    assert pair(1, 0, 0) == 1
    assert pair(0, 0, 1) == 2
    assert pair(0, 1, 0) == 3
    assert pair(1, 0, 1) == 4
    assert pair(0, 0, 2) == 5
    assert pair(2, 0, 0) == 6
    assert pair(0, 1, 1) == 7
    assert pair(1, 0, 2) == 8
    assert pair(0, 0, 3) == 9
    assert pair(1, 1, 0) == 10

def test_depair():
    #1D
    for n in range(100):
        assert depair(n, d=1) == (n,)
    #2D
    assert depair(0) == (0, 0)
    assert depair(1) == (1, 0)
    assert depair(2) == (0, 1)
    assert depair(3) == (2, 0)
    assert depair(4) == (1, 1)
    assert depair(5) == (0, 2)
    assert depair(6) == (3, 0)
    assert depair(7) == (2, 1)
    assert depair(8) == (1, 2)
    assert depair(9) == (0, 3)
    #3D
    assert depair(0, d=3) == (0, 0, 0)
    assert depair(1, d=3) == (1, 0, 0)
    assert depair(2, d=3) == (0, 0, 1)
    assert depair(3, d=3) == (0, 1, 0)
    assert depair(4, d=3) == (1, 0, 1)
    assert depair(5, d=3) == (0, 0, 2)
    assert depair(6, d=3) == (2, 0, 0)
    assert depair(7, d=3) == (0, 1, 1)
    assert depair(8, d=3) == (1, 0, 2)
    assert depair(9, d=3) == (0, 0, 3)
    assert depair(10, d=3) == (1, 1, 0)

def test_pair_and_unpair():
    for d in (1, 2, 3, 4):
        for n in range(100):
            assert pair(*depair(n, d=d)) == n

def test_gen():
    for n, i in enumerate(islice(gen(), 100)):
        assert depair(n) == i
