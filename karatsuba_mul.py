import random

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y))) // 2
    a = x // (10**n)
    b = x % 10**n
    c = y // (10**n)
    d = y % 10**n
    ac, bd = karatsuba(a, c), karatsuba(b, d)
    ad_bc = karatsuba(a+b, c+d) - ac - bd
    return (ac * 10**(2*n)) + (ad_bc * 10**n) + bd



def test():
    for j in range(4):
        for i in range(1000):
            x = random.randint(1,10**7)
            y = random.randint(1,10**7)
            expected = x * y
            result = karatsuba(x, y)
            if result != expected:
                print(f"Test {j+1} failed!")
                return
        print(f'Test {j+1} passed!')

test()
