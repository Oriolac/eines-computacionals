

def division(a: int, b: int):
    q = 0
    while a >= b:
        a -= b
        q += 1
    return q, a

def trial_division(n: int):
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

def smallest_prime_number(min:int):
    for i in range(min+1, 10010**2):
        if trial_division(i):
            return i

def test_division():
    print(division(3,2))
    print(division(49, 7))
    print(division(48, 7))
    print(division(50, 7))

def test_trial_division():
    print(trial_division(7))
    print(trial_division(8))
    print(trial_division(2))
    print(trial_division(1))
    print(trial_division(3))
    print(trial_division(6))

def main():
    test_division()
    test_trial_division()
    print(smallest_prime_number(10010))

if __name__ == "__main__":
    main()