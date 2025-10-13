"""Szudzik pairing variation.

The leg filling is interweaved.

![plot](szudzik2.png)

References
----------
- [David R Hagen: Superior Pairing Function - Peter pairing function](https://drhagen.com/blog/superior-pairing-function/#peter-pairing-function)
"""



from math import isqrt



__all__ = ('pair', 'depair')



def pair(i, j):
    """Return the paired number.
    
    Szudzik pairing function variation.
    """
    assert isinstance(i, int) and i>=0 and isinstance(j, int) and j>=0, 'Can only pair two non-negative integers'
    shell = max(i, j)
    step = min(i, j)
    return shell**2 + step*2 + int(step!=i)

def depair(n):
    """Return the depaired numbers.
    
    Szudzik pairing function variation inverse.
    """
    assert isinstance(n, int) and n>=0, 'Can only depair a non-negative integer'
    shell = isqrt(n)
    remainder = n - shell**2
    step = remainder // 2
    if remainder%2 == 0:  # remainder is even
        return (step, shell)
    else:
        return (shell, step)
