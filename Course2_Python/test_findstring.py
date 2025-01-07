from curses.ascii import isdigit
import pytest
import findstring

def test_ispresent():
    assert findstring.ispresent("Al")
    
def test_nodigit():
    assert findstring.nodigit("N7")