# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: just520fun
@Prime numbers in setctions
"""

import math
from timeit import default_timer as timer

def isprime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0: #no even
        return False
    for i in range(3,int(math.sqrt(num)+1),2): #3~sqrt(num)+1, odd only
        if num%i == 0:
            return False
    else:
        return True
    
if __name__ == '__main__':
    print('prime number')
    tic=timer()
    
    #prime number sections
    #S1 1 72
    #S2 73 216
    #S3 217 432
    #s4 433 720
    #S5 721 1080
    #S6 1081 1512
    #S7 1513 2016
    #S8 2017 2592
    #S9 2593 3240
    #S10 3241 3960
    #...
    #Sn S(n-1)max+1 +36*(n*2)-1
    #or
    #Sn n*(n-1)/2*2*36+1 n*(n+1)/2*2*36
    
    secstart= 1 #Section start no.
    secstop= 1000 #Section stop no.
    
    i=secstart
    pnstart=int(secstart*(secstart-1)/2*2*36+1)
    pnfile=open("log.txt","a+")
    pnfile.write("Total range:"+str(int(secstart*(secstart-1)/2*2*36+1))+"~"+str(int(secstart*(secstart+1)/2*2*36))+"\n")
    pnfile.close()
    print("Total range:"+str(int(secstart*(secstart-1)/2*2*36+1))+"~"+str(int(secstart*(secstart+1)/2*2*36))+"\n")
    
    while i<=secstop:
        pnrange="S"+str(i)
        pnstop=pnstart+36*(i*2)-1
        pnfile=open(pnrange+"("+str(pnstart)+"~"+str(pnstop)+").txt","w")
        pnfile.write(pnrange+"("+str(pnstart)+"~"+str(pnstop)+")\n")
        print(pnrange+"("+str(pnstart)+"~"+str(pnstop)+")\n")
        count=0
        
        if pnstart==1:
            for num in range(pnstart,pnstop,1): #1 2 3 should be considered
                if isprime(num):
                    pnfile.write(str(num)+"\n")
                    count=count+1
        else:
            for num in range(pnstart,pnstop,2): #odd only
                if isprime(num):
                    pnfile.write(str(num)+"\n")
                    count=count+1
            
                    
        pnstart=pnstop+1
        i=i+1
        pnfile.write("There are "+str(count)+" prime numbers in "+pnrange+".\n")
        pnfile.close()
        
    toc=timer()
    print("It takes ",toc-tic, " s.\n") #time
    
#END

#optimaztion
#isprime algorithm complexit n/(2~n-1) is o(n^2)
#divided from 2~n-1 to 3~sqrt(n)+1 (2 as special number) => algorithm complexity o(n^1.5)
#divide number from x0~x9 to X1 X3 x7 x9 while x>=1 =>complexity *4/10
#python os.nice CPU priority  DOES NOT work porperly in Windows
#Multi-thread or Multi-process for multocore CPU

#More usage
#prime matrix
#Build a prime number matrix for big enough range (2~1trillion)
#Search the prime number the matrix
    
    
#Please see https://en.wikipedia.org/wiki/Prime_number


#More deep optimization with CPU vector instruction(ISA)
#prime95 with FFT assembly code over Intel AVX-512
#please see https://www.mersenne.org

#《Experience of Optimizing FFT on Intel Architectures》 
# http://www.capsl.udel.edu/pub/doc/papers/POHLL2007-Daniel.pdf

# Or even more deep dive to DSP/FPGA or even ASIC    
    
