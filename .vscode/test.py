
def func(x,y):
    z = x+y
    return z 

def test_a(xx,yy):
    z = xx * yy
    k = xx / yy
    return z , k
    
if __name__ == '__main__':

    try:
        func(50,20)
        test_a(10,2)
        pass
    except Exception as e:
        print('따시')
        pass
