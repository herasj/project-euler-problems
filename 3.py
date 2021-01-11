# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math
#Vars
number = 600851475143
factor = 2

def isPrime(num):
    i=5

    if(num==2 or num==3):
        return True

    if(num%2==0 or num%3 ==0 or num<=1):
        return False

    while(i**2<=num):
        if(num%i==0 or num%(i+2)==0):
            return False
        i+=6
    return True

while(number>1):
    if(number%factor==0):
        number /= factor
        if(isPrime(factor)):
            print('Prime Factor: ', factor)
            factor= factor
        else:
            print('Not prime: ', factor)
    else:
        factor+=1
print("")
print("Answer: ",factor)