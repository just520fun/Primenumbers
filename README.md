# Primenumbers
 Prime numbers algorithm in 36N sections


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

