#-*- coding: utf-8 -*
'''
Created on 14/10/2017

'''
# This is a ARS Primality Test written in python 3

'''
def expand_x_1(n):
    # This version uses a generator and thus less computations
    c = 1
    for i in range(n / 2 + 1):
        c = c * (n - i) / (i + 1)
        yield c


def aks(p):
    if p == 2:
        return True

    for i in expand_x_1(p):
        if i % p:
            # we stop without computing all possible solutions
            return False
    return True
'''


def expand_x_1(num):
    ex = [1]
    if num >= 2:
        for i in range(num):
            ex.append(ex[-1] * -(num - i) / (i + 1))
        return ex[::-1]
 
def aks_test(num):
    ex = expand_x_1(num)
    ex[0] += 1
    return not any(mult % num for mult in ex[0:-1])
 



'''
print('# p: (x-1)^p for small p')
for p in range(12):
    print('%3i: %s' % (p, ' '.join('%+i%s' % (e, ('x^%i' % n) if n else '')
                                   for n,e in enumerate(expand_x_1(p)))))
 
print('\n# small primes using the aks test')
print([p for p in range(101) if aks_test(p)])

