# -*- coding: utf-8 -*
"""
Created on 01/11/2017

"""

def plain_list(N):
    primes = []
    for num in range(N, N+1000):
        if all(num % i != 0 for i in range(2, num)):
            primes.append(num)
    return primes

lis=plain_list(192)
print(lis[0:5:1])