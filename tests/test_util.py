from pairings.util import *



def test_shell():
    assert shell(0, 0, form='diagonal') == 0
    assert shell(0, 1, form='diagonal') == 1
    assert shell(1, 0, form='diagonal') == 1
    assert shell(0, 2, form='diagonal') == 2
    assert shell(1, 1, form='diagonal') == 2
    assert shell(2, 0, form='diagonal') == 2
    assert shell(0, 3, form='diagonal') == 3
    assert shell(1, 2, form='diagonal') == 3
    assert shell(2, 1, form='diagonal') == 3
    assert shell(3, 0, form='diagonal') == 3
    assert shell(0, 4, form='diagonal') == 4
    assert shell(1, 3, form='diagonal') == 4
    assert shell(2, 2, form='diagonal') == 4
    assert shell(3, 1, form='diagonal') == 4
    assert shell(4, 0, form='diagonal') == 4
    
    assert shell(0, 0, form='cubic') == 0
    assert shell(0, 1, form='cubic') == 1
    assert shell(1, 0, form='cubic') == 1
    assert shell(1, 1, form='cubic') == 1
    assert shell(0, 2, form='cubic') == 2
    assert shell(1, 2, form='cubic') == 2
    assert shell(2, 2, form='cubic') == 2
    assert shell(2, 1, form='cubic') == 2
    assert shell(2, 0, form='cubic') == 2
    assert shell(0, 3, form='cubic') == 3
    assert shell(1, 3, form='cubic') == 3
    assert shell(2, 3, form='cubic') == 3
    assert shell(3, 3, form='cubic') == 3
    assert shell(3, 2, form='cubic') == 3
    assert shell(3, 1, form='cubic') == 3
    assert shell(3, 0, form='cubic') == 3
