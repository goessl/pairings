r"""Rosenberg-Strong pairing variation.

The shells are filled in alternating order.

![plot](rosenberg_strong2.png)

References
----------
- [David R Hagen - Superior Pairing Function - Peter pairing function](https://drhagen.com/blog/superior-pairing-function/#peter-pairing-function)
"""



from .rosenberg_strong import pair as pair1, depair as depair1
from math import isqrt



__all__ = ('pair', 'depair')



def pair(i, j):
    """Return the paired number.
    
    Rosenberg-Strong pairing variation function.
    """
    shell = max(i, j)
    return pair1(i, j) if int(shell%2) else pair1(j, i)

def depair(n):
    """Return the depaired numbers.
    
    Rosenberg-Strong pairing function variation inverse.
    """
    i, j = depair1(n)
    shell = isqrt(n)
    return (i, j) if int(shell%2) else (j, i)
