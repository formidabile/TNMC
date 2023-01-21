from timeit import default_timer as timer

def evklid(a, b):
    x2 = 1; x1 = 0
    y2 = 0; y1 = 1
    r = 0; q = 0
    i = 0; x = 0; y = 0
    print("i |          a            | x | y | q")
    print("-------------------------------------")
    print(f'{i + 1} | {a} | {x2} | {y2} |')
    while (b > 0):
        q = a // b
        r = a % b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b; b = r; x2 = x1; x1 = x; y2 = y1; y1 = y
        i += 1
        print(f'{i + 1} | {a} | {x2} | {y2} | {q}')
    x = x2; y = y2
    return a, x, y

def binary_evklid(a, b):
    g = 1
    while (a % 2 == b & 2 == 0):
        a //= 2
        b //= 2
        g *= 2
    u = a; v = b; A = 1; B = 0; C = 0; D = 1
    i = 0
    print("i |          u            | A | B |          q           | C | D")
    print("-------------------------------------")
    print(f'{i} | {u} | {A} | {B} | {v} | {C} | {D}')
    while (u != 0):
        while (u % 2 == 0):
            u //= 2
            if (A % 2 == B % 2 == 0):
                A //= 2
                B //= 2
            else:
                A = (A + b) // 2
                B = (B - a) // 2
        while (v % 2 == 0):
            v //= 2
            if (C % 2 == D % 2 == 0):
                C //= 2
                D //= 2
            else:
                C = (C + b) // 2
                D = (D - a) // 2
        if (u >= v):
            u -= v
            A -= C
            B -= D
        else:
            v -= u
            C -= A
            D -= B
        print (f'{i + 1} | {u} | {A} | {B} | {v} | {C} | {D}')
        i += 1
    return  g * v, C, D

def trunc_evklid(a, b):
    x2 = 0; x1 = 1
    y2 = 1; y1 = 0
    r = 0; q = 0
    i = 0; x = 0; y = 0
    print("i |          a            | x | y | q")
    print("-------------------------------------")
    print(f'{i + 1} | {a} | {x2} | {y2} |')
    while (b > 0):
        q = a // b
        r = a % b
        x = x1 - q * x2
        y = y1 - q * y2
        x1 = x2; y1 = y2
        x2 = x; y2 = y
        if (abs(a) > abs(b) // 2):
            a -= b
            x -= x1
            y -= y1
        a = b; b = r
        i += 1
        print(f'{i + 1} | {a} | {x2} | {y2} | {q}')
    # x = x2; y = y2
    return abs(a), x, y

def main():
    a1 = 26041024811993384483; b1 =9266310508585114561
    a2 = 1505719777417098948174456280835440228447; b2 = 521642581518998345636821873435766199247
    a3 = 97728974248515269025607020472352959665345151320152027788833105868611280309672717; b3 = 78292958273482336866858065534433713374060164757847335305130442573946774600486691
    a = a1; b = b1
    start = timer()
    d, x, y = evklid(a, b)
    #d, x, y = binary_evklid(a, b)
    #d, x, y = trunc_evklid(a, b)
    print('\nLinear view: \n' + f'{d} = {a} * {x} + {b} * {y}' + '\n')
    print('Total time: ' + f'{format(timer() - start)}' + ' secs')

if __name__ == '__main__':
    main()