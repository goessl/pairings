# pairings

A pairing functions Python package.
```python
>>> from pairings.nz import unfold
>>> for n in range(9):
...     print(n, unfold(n))
...
0 0
1 -1
2 1
3 -2
4 2
5 -3
6 3
7 -4
8 4
```

## Installation

```console
pip install git+https://github.com/goessl/pairings.git
```

## Usage

|           | [`nz`](nz.md)                           | [`nz2`](nz2.md)                         | [`cantor`](cantor.md)                       |
| --------- | --------------------------------------- | --------------------------------------- | ------------------------------------------- |
| Domains   | $\mathbb{N}_0\leftrightarrow\mathbb{Z}$ | $\mathbb{N}_0\leftrightarrow\mathbb{Z}$ | $\mathbb{N}_0\leftrightarrow\mathbb{N}_0^d$ |
| Forward   | [`nz.fold`][pairings.nz.fold]            | [`nz2.fold`][pairings.nz2.fold]          | [`cantor.pair`][pairings.cantor.pair]        |
| Backwards | [`nz.unfold`][pairings.nz.unfold]        | [`nz2.unfold`][pairings.nz2.unfold]      | [`cantor.depair`][pairings.cantor.depair]    |
| Generator | [`nz.gen`][pairings.nz.gen]              | [`nz2.gen`][pairings.nz2.gen]            | [`cantor.gen`][pairings.cantor.gen]          |

## Roadmap

- Foldings
    - [x] $\mathbb{N}_0 \leftrightarrow \mathbb{Z}$
- Pairings
    - Bijections
        - [x] Cantor
        - [ ] Hopcroft-Ullman
        - [ ] Regan
        - [ ] Pigeon
        - [ ] Szudzik
    - Utility
        - [ ] Generalizer to higher dimensions
        - [ ] Generalizer to $\mathbb{Z}^2$
        - [ ] Generalizer for shifts?
        - [ ] Sort into diagonal-, square-, Morton-?, hyperbolic, ... shell fillers
        - [ ] plots with norm comparisons
- Rationals
    - [ ] Farey
- Algebraic?

## License (MIT)

Copyright (c) 2025 Sebastian Gössl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
