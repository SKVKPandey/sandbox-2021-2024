def MyFun(val):
    val = str(val)
    if val == val[::-1]:
        return True
    else:
        return False

#[starting, terminating - 1, increment]

try:
    print(MyFun(123456789))
except Exception as e:
    print(e)
finally:
    print("Try and Except has been called")