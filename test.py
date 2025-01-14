from payment import calculate as cal

def test(a,b):
    assert cal(a,b) == a-b

test(10,20)
test(1,15)
test(40,150)
