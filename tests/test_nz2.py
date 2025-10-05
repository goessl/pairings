from itertools import islice
from pairings.nz2 import *



def test_unfold():
    assert unfold(0) == 0
    assert unfold(1) == +1
    assert unfold(2) == -1
    assert unfold(3) == +2
    assert unfold(4) == -2
    assert unfold(5) == +3
    assert unfold(6) == -3
    assert unfold(7) == +4
    assert unfold(8) == -4

def test_fold():
    assert fold(0) == 0
    assert fold(+1) == 1
    assert fold(-1) == 2
    assert fold(+2) == 3
    assert fold(-2) == 4
    assert fold(+3) == 5
    assert fold(-3) == 6
    assert fold(+4) == 7
    assert fold(-4) == 8

def test_fold_and_unfold():
    for n in range(100):
        assert fold(unfold(n)) == n
    for i in range(-50, +50):
        assert unfold(fold(i)) == i

def test_gen():
    for n, i in enumerate(islice(gen(), 100)):
        assert unfold(n) == i
