r"""Cantor pairing.

$$
    \mathbb{N}_0 \leftrightarrow \mathbb{N}_0^d
$$

References
----------
- [Wikipedia - Pairing function - Cantor pairing function](https://en.wikipedia.org/wiki/Pairing_function#Cantor_pairing_function)
- [Wikipedia - Cantorsche Paarungsfunktion](https://de.wikipedia.org/wiki/Cantorsche_Paarungsfunktion)
- [Wolfram MathWorld - Pairing Function](https://mathworld.wolfram.com/PairingFunction.html)
"""



from math import isqrt
from functools import reduce



__all__ = ('pair', 'depair')



def pair(*k):
    r"""Return the paired number.
    
    $$
        \begin{aligned}
            \pi(k_1, k_2) = \pi^{(2)}(k_1, k_2) &= \frac{(k_1+k_2)(k_1+k_2+1)}{2}+k_2 \\
            \pi^{(n)}(k_1, k_2, \dots, k_n) &= \pi\left(\pi^{(n-1)}(k_1, \dots, k_{n-1}), k_n\right)
        \end{aligned} \qquad \mathbb{N}_0^d\to\mathbb{N}_0
    $$
    
    Cantor pairing function.
    """
    assert len(k) >= 1, 'Can only pair one or more values'
    for ki in k:
        assert isinstance(ki, int) and ki>=0, 'Can only pair non-negative integers'
    return reduce(lambda k1, k2: (k1+k2)*(k1+k2+1)//2+k2, k)

def depair(z, d=2):
    r"""Return the depaired numbers.
    
    $$
        \pi^{-1}(z) \qquad \mathbb{N}_0\to\mathbb{N}_0^d
    $$
    
    Cantor pairing function inverse.
    """
    assert isinstance(z, int) and z>=0 \
            and isinstance(d, int) and d>=1, 'Can only depair a non-negative integer into one or more values'
    i = [z]
    while len(i) < d:
        w = (isqrt(8 * i[0] + 1) - 1) // 2
        t = (w**2 + w) // 2
        i[0:1] = [w-(i[0]-t), i[0]-t]
    return tuple(i)
