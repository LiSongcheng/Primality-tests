#-*- coding: utf-8 -*
'''
Created on 14/10/2017

'''
# This is a Sieve of Eratosthesis method
'''
1. list all numbers in range
2. circling all multiples of 2 by N
3. the continue circling the multiples of the consecutive prime, e.g. 3
4. stop sieving when you have the number last that last > sqrt(N), e.g.
    120, stop by 11 since sqrt(12) = 10.95, and 11^2 = 121
5. the remaining numbers are primes.
multithreading?
'''

def sieve_list(N):
    primes = []
    for i in range(0, N):
        if sieve_array(N)[i]:
            primes.append(i + 1)
    # or use numpy.nonzero(); primes = nonzero(ary)[0] + 1
    return primes


def sieve_array(N):
    import math
    from numpy import ones
    ary = ones(N, dtype = bool)
    for i in range(2, math.ceil(N) + 1): # sieving
        if ary[i - 1]: # omitted 1, primes
            ary[range(2 * i - 1, N, i)] = False
    return ary

# print(sieve_list(100))