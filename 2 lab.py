from random import randint

def ferma(n):
    a = randint(2, n - 2)
    r = pow(a, n - 1, n)
    if r == 1:
        return 0, a
    return 1, a

def jakobi(a, n):
    g = 1
    while 1:
        k = 0
        s = 0
        if a == 0:
            return 0
        if a == 1:
            return g
        a1 = a
        while (a1 % 2 == 0):
            a1 //= 2
            k += 1
        if k % 2 == 0:
            s = 1
        else:
            if n % 8 == 1 or n % 8 == 7:
                s = 1
            if n % 8 == 3 or n % 8 == 5:
                s = -1
        if a1 == 1:
            return g * s
        if n % 4 == a1 % 4 == 3:
            s = -s
        a = n % a1
        n = a1
        g = g * s

def solovai_strassen(n):
    a = randint(2, n - 2)
    r = pow(a, (n - 1) // 2, n)
    if r != 1 and r != n - 1:
        return 1, a
    s = jakobi(a, n)
    if r != s % n:
        return 1, a
    return 0, a

def rabin_miller(n):
    a = randint(2, n - 2)
    r = n - 1
    s = 0
    while r % 2 == 0:
        r //= 2
        s += 1
    y = pow(a, r, n)
    while y != 1 and y != n - 1:
        j = 1
        while j <= s - 1 and y != n - 1:
            y = pow(y, 2, n)
            if y == 1:
                return 1, a
            j += 1
        if y != n - 1:
            return 1, a
    return 0, a

def main():
    a1 = 26038194109534512481
    a2 = 5128760265312481480874401826277265910263
    a3 = 1066988516336777184965728135501202723287
    a4 = 39949053819256873245394672333354348234401053789710301065757537726978417641957291
    c1 = 32809426840359564991177172754241
    c2 = 2810864562635368426005268142616001
    print(f"Тест Ферма для числа Кармайкла {c1}: \n")
    for i in range(5):
        r, a = ferma(c1)
        #r, a = solovai_strassen(c1)
        #r, a = rabin_miller(c1)
        if r == 1:
            print(f"Число составное, основание {a}")
            break
        else:
            print(f"Число n, вероятно, простое, основание {a}")

if __name__ == '__main__':
    main()