import pytest

def createFile():
    f = open("helloworld.txt", "x")




def test_createFile():
    # assert will return true or raise an AssertionError
    # the primary application is debugging
    assert exists("helloworld.txt") in str(createFile())
