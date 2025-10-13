"""Szudzik pairing variation.

The leg filling is interweaved and they are started alternatingly.

![plot](szudzik3.png)

References
----------
- [David R Hagen: Superior Pairing Function - Alternative pairing function](https://drhagen.com/blog/superior-pairing-function/#alternative-pairing-function)
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
    if shell%2==0 and step==j or shell%2==1 and step==i:
        flag = 0
    else:
        flag = 1
    return shell**2 + step*2 + flag

def depair(n):
    """Return the depaired numbers.
    
    Szudzik pairing function variation inverse.
    """
    assert isinstance(n, int) and n>=0, 'Can only depair a non-negative integer'
    shell = isqrt(n)
    step = (n - shell**2) // 2
    if n%2 == 0:  # index is even
        return (shell, step)
    else:
        return (step, shell)
