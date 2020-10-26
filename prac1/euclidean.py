

def euclidean(a: int, b: int):
    if a % b == 0:
        if b == 1:
            return 1, 1
        else:
            return int(a / b), 1
    else:
        res = euclidean(b, a % b)
        return res[0], res[1] + 1


def extended_euclidean(a: int, b: int):
    prevx, x = 1, 0
    prevy, y = 0, 1
    steps = 0
    while b:
        q = int(a / b)
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
        a, b = b, a % b
        steps += 1
    return a, prevx, prevy, steps


def test():
    print("TEST:")
    print(euclidean(11, 7))
    print(euclidean(6, 2))
    print(euclidean(35, 30))


def p2():
    print(euclidean(487669403177, 28736540321))
    print(euclidean(20365011074, 12586269025))
    print(euclidean(2**35-1, 2**34-1))


def p3():

    def xtest(a, b):
        d, s, t, st = extended_euclidean(a, b)
        print(f"{s} * {a} + ({t}*{b}) = {d}; steps: {st}")
    xtest(11, 7)
    xtest(487669403177, 28736540321)
    xtest(20365011074, 12586269025)
    xtest(2 ** 35 - 1, 2 ** 34 - 1)


def p4():
    def inverse(m, a):
        _, _, t, _ = extended_euclidean(m, a)
        if t < 0:
            t = t + m
        print(f"inverse of {a} (mod {m}) = {t}")
    inverse(11, 7)
    inverse(487669403177, 28736540321)
    inverse(20365011074, 12586269025)


def main():
    test()
    p2()
    p3()
    p4()


if __name__ == "__main__":
    main()
