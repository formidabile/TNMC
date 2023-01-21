from random import randint
import math

def f(x, n):
    return (x ** 2 + 1) % n

def gcd(a, b):
    r1, r2 = a, b
    while r2 != 0:
        r1, r2 = r2, r1 % r2
    return r1

def prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def po_pollard(n):
    with open("output.txt", "w") as file:
        i = 1
        a, b = 2, 2
        d = 1
        #file.write(f"{i} : a = {a}, b = {b}, gcd = {d}")
        print(f"{i} : a = {a}, b = {b}, gcd = {d}")
        while (d == 1):
            i += 1
            a = f(a, n)
            b = f(f(b, n), n)
            d = gcd(a - b, n)
            #file.write(f"{i} : a = {a}, b = {b}, gcd = {d}\n")
            print(f"{i} : a = {a}, b = {b}, gcd = {d}")
            if 1 < d < n:
                return d
            if d == n:
                return -1

def p1_pollard(n):
    with open("output.txt", "w") as file:
        a = randint(2, n - 2)
        d = gcd(a, n)
        #file.write(f"{0} : a = {a}, gcd = {d}\n")
        print(f"{0} : a = {a}, gcd = {d}")
        if d >= 2:
            return d
        p = 3
        i = 1
        while 1:
            l = math.log(n) // math.log(p)
            a = pow(a, pow(p, int(l)), n)
            d = gcd(a - 1, n)
            #file.write(f"{i} : base = {p}, l = {int(l)}, a = {a}, gcd = {d}\n")
            print(f"{i} : base = {p}, l = {int(l)}, a = {a}, gcd = {d}")
            i += 1
            if d != 1 and d != n:
                return d
            p += 1
            while(prime(p) == False):
                p += 1
            if p > n:
                return -1


def main():
    n1 = 38832860457845472649
    n2 = 238383131369419463647743663032226432533
    n3 = 49002025318013248697147170464805529233284300285792526768332193728325507685973121
    n, m = 2023, 2023
    base = []
    while 1:
        res = p1_pollard(n)
        #if res == -1:
        #    break
        print(f"{n} = {res} * {n // res}")
        if res == -1:
            break
        if prime(res) == False:
            base.append(n // res)
            n = res
            continue
        base.append(res)
        if prime(n // res):
            base.append(n // res)
            break

        n //= res
    print(base)
    print(f"{m} = ", end='')
    for i in base:
        print(f"{i} * ", end='')
    #print(n3 ** (1 / 2) * math.log(n3) * 8 / (385394 * 3600 * 24 * 365))
    #print(p1_pollard(2023))

if __name__ == '__main__':
    main()