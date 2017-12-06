#-*- coding: utf-8 -*
'''
Created on 14/10/2017

'''

if __name__=="__main__":
    import func

    print('1. write an analysis based on \
    Computational Complexity theory, \
    and check with the book <Algorithm>./n')

    print('2. write func descriptions in the\
    style of official funcs./n')

    '''
    for size in range(1,8):
        max_number=10**size
        t1=clock()
        primes=Sieve(max_number)
        t2=clock()
        t=t2-t1
        time_per_n=t/max_number
        print "{} (primes to {}) took {} secs ({} secs/number for {} primes".format(size,max_number,t,time_per_n,len(primes))
    '''

    print(funcSieve(10))