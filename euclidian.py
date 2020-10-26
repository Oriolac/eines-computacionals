#!/usr/bin/env python3

import logging


def division(divident: int, divisor: int):
    quocient: int = 0
    while divisor <= divident:
        divident -= divisor
        quocient += 1
    remainder = divident
    return quocient, remainder


def trial_division(n: int):
    for p in range(2, int(n / 2) + 1):
        q, r = division(n, p)
        if r == 0:
            return p, q
    return None


def smallest_prime_number(threshold: int):
    for i in range(threshold, threshold * 2):
        if trial_division(i) is None:
            return i
    return smallest_prime_number(threshold * 2)


def euclidian(a: int, b: int):
    a, b = division(a, b)
    print(a, b)
    if b == 0:
        return a
    return euclidian(a, b)
