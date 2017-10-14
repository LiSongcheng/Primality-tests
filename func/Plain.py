# -*- coding: utf-8 -*
"""
Created on 14/10/2017

"""
# This is a Plain Method of find Primes

def plain_check(num):
    list = []
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

def plain_list(N):
    primes = []
    for i in range(2, N + 1):
        if plain_check(i):
            primes.append(i)
    return primes


# print(plain_list(120))