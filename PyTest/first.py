import pytest

def my_func(x,y,z):
    return x+y+z

def test_result():
    assert my_func(1,2,3)!=36
def my_exception():
    div = 10/0
    return div
class TestClass(object):
    def test_result(self):
        assert my_func(1,2,2)==5
    def test_result2(self):
        assert my_func(1,2,3)==6
def test_result3():
    with pytest.raises(ZeroDivisionError):
        my_exception()