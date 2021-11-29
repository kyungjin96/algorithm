
def func(x,y):
    z = x+y
    return z 

def test_a(x,y):
    z = x * y
    k = x / y
    return z , k
    

if __name__ == '__main__':
    try:
        func(50,20)
        test_a(10*0)
        pass
    except Exception as e:
        print('typeError')
        pass
