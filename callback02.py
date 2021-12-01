def fun_collback(a):
    print('fun_callback sum : ',a)
    return



def fun_call(x, y, f_callback):
    resrult = x + y
    f_callback(resrult)
    return 

first = 10
second = 20
fun_call(first, second, fun_collback)



# if __name__ == '__main__':
#     try:
#         pass
#     except Exception as e:
#         pass
