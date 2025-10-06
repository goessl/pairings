from pairings import cantor2, cantor



def test_pair():
    for i in range(100):
        for j in range(100):
            assert cantor2.pair(i, j) == cantor.pair(j, i)

def test_depair():
    for n in range(100):
        assert cantor2.depair(n) == tuple(reversed(cantor.depair(n)))
