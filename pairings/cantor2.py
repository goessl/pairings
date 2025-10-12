"""Cantor pairing variation.

Flipped version of [`cantor`](cantor.md).

![plot](cantor2.png)
"""



from math import isqrt



__all__ = ('pair', 'depair')



def pair(i, j):
    """Return the paired number.
    
    Cantor pairing function variation.
    """
    assert isinstance(i, int) and i>=0 and isinstance(j, int) and j>=0, 'Can only pair two non-negative integers'
    return (i + j) * (i + j + 1) // 2 + i

def depair(z):
    """Return the depaired numbers.
    
    Cantor pairing function variation inverse.
    """
    assert isinstance(z, int) and z>=0, 'Can only depair a non-negative integer'
    w = (isqrt(8 * z + 1) - 1) // 2
    t = (w**2 + w) // 2
    return (z-t, w-(z-t))
