r"""Rosenberg-Strong pairing.

References
----------
- [Matthew P. Szudzik: The Rosenberg-Strong Pairing Function - Chapter 2](https://arxiv.org/pdf/1706.04129)
"""



from math import isqrt
from itertools import count



__all__ = ('pair', 'depair', 'gen')



def pair(x, y):
    """Return the paired number.
    
    Rosenberg-Strong pairing function.
    """
    assert isinstance(x, int) and x>=0 and isinstance(y, int) and y>=0, 'Can only pair two non-negative integers'
    r = max(x, y)
    return r**2 + r + x - y

def depair(z):
    """Return the depaired numbers.
    
    Rosenberg-Strong pairing function inverse.
    """
    assert isinstance(z, int) and z>=0, 'Can only depair a non-negative integer'
    m = isqrt(z)
    if z-m**2 < m:
        return (z-m**2, m)
    else:
        return (m, m**2+2*m-z)

def gen(start=0):
    """Yield Rosenberg-Strong pairing function tuples."""
    for z in count(start):
        yield depair(z)
