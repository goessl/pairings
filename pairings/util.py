"""Utility functions."""



__all__ = ('shell', )



def shell(i, j, form):
    """Return the shell index.
    
    ![plot](shells.png)
    
    Available forms are:
    
    - `diagonal` &
    - `cubic`.
    
    References
    ----------
    - [Matthew P. Szudzik: The Rosenberg-Strong Pairing Function](https://arxiv.org/pdf/1706.04129) Definition 2.1
    """
    assert isinstance(i, int) and i>=0 \
            and isinstance(j, int) and j>=0, 'Can determine shell for two non-negative integers.'
    match form:
        case 'diagonal':
            return i + j
        case 'cubic':
            return max(i, j)
        case _:
            raise ValueError('Invalid form')
