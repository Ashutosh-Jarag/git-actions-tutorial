from src.main import add,sub,mul,div

def test_add():
    assert add(2,3) == 5
    assert add(5,1) == 6


def test_sub():
    assert sub(2,3) == -1
    assert sub(1-1) == 0
    assert sub(10-5) == 5

def test_mul():
    assert mul(2,3) == 6
    assert mul(4,4) == 16
# def test_div():
#     assert div(2,3) == 0.6666666666666666