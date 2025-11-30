#This code calculates the sum of the prime number below 2 milion.
#Problem address : https://projecteuler.net/problem=10
def FindPrimeNumber(number):
    state=0
    for i in range(2,(number//2)+1):
        if number%i == 0 :
            state+=1
    if state==0 :
        return True
    else:
        return False

def sumOfThePrimeNumbers(limit=2000000):
    num=2
    sum=0
    while( num<=limit):
        if FindPrimeNumber(num):
            sum+=num
        num+=1
    print(sum)


sumOfThePrimeNumbers(11)
