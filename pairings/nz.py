r"""Canonical bijection between natural numbers and whole integers.

$$
    \mathbb{N}_0 \leftrightarrow \mathbb{Z}
$$

![plots](nz.png)

| $\mathbb{N}_0$ | $\leftrightarrow$ | $\mathbb{Z}$ |
| -------------- | ----------------- | ------------ |
|              0 | $\leftrightarrow$ |            0 |
|              1 | $\leftrightarrow$ |           -1 |
|              2 | $\leftrightarrow$ |           +1 |
|              3 | $\leftrightarrow$ |           -2 |
|              4 | $\leftrightarrow$ |           +2 |
|              5 | $\leftrightarrow$ |           -3 |
|              6 | $\leftrightarrow$ |           +3 |
|              7 | $\leftrightarrow$ |           -4 |
|              8 | $\leftrightarrow$ |           +4 |
|                | $\vdots$          |              |

See also
--------
- Zig-zag function
- Canonical bijection between $\mathbb{N}_0$ & $\mathbb{Z}$
- [Folding function](https://mathworld.wolfram.com/FoldingFunction.html)

References
----------
- [Wolfram MathWorld - Folding function](https://mathworld.wolfram.com/FoldingFunction.html)
- [Wikipedia - Bijection - More mathematical examples](https://en.wikipedia.org/wiki/Bijection#More_mathematical_examples)
"""



from itertools import count



__all__ = ('fold', 'unfold', 'gen')



def fold(i):
    r"""Return `i` folded from the whole integers to the natural numbers.
    
    $$
        f(i)=\begin{cases}
            2i & i\geq0 \\
            2|i|-1 & i\lt0
        \end{cases} \qquad \mathbb{Z}\to\mathbb{N}_0
    $$
    """
    assert isinstance(i, int), 'Can only fold whole integers.'
    return 2*i if i>=0 else -2*i-1

def unfold(n):
    r"""Return `n` unfolded from the natural numbers to the whole integers.
    
    $$
        f^{-1}(n)=\begin{cases}
            \frac{n}{2} & n\in\mathbb{G} \\
            -\frac{n+1}{2} & n\in\mathbb{U}
        \end{cases} \qquad \mathbb{N}_0\to\mathbb{Z}
    $$
    """
    assert isinstance(n, int) and n>=0, 'Can only unfold natural numbers.'
    return -(n+1)//2 if bool(n%2) else n//2

def gen(start=0):
    r"""Yield whole integers in increasing absolute value.
    
    $$
        \left(f^{-1}(n)\right)_{n\in\mathbb{N}_0} = (0, -1, +1, -2, +2, -3, +3, -4, +4, \dots)
    $$
    """
    assert isinstance(start, int) and start>=0, 'Can only unfold natural numbers.'
    for n in count(start):
        yield unfold(n)
