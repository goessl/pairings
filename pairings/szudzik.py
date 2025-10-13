"""Szudzik pairing.

![plot](szudzik.png)

References
----------
- [Szudzik: Elegant Pairing](http://szudzik.com/ElegantPairing.pdf)
"""



from math import isqrt



__all__ = ('pair', 'depair')



def pair(i, j):
    """Return the paired number.
    
    Szudzik pairing function.
    """
    assert isinstance(i, int) and i>=0 and isinstance(j, int) and j>=0, 'Can only pair two non-negative integers'
    if i < j:
        return j**2 + i
    else:
        return i**2 + i + j

def depair(z):
    """Return the depaired numbers.
    
    Szudzik pairing function inverse.
    """
    assert isinstance(z, int) and z>=0, 'Can only depair a non-negative integer'
    m = isqrt(z)
    if z - m**2 < m:
        return (z-m**2, m)
    else:
        return (m, z-m**2-m)
