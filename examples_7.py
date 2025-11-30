#Th,s code finds the 10001st prime number...
#ProjectEuler problem 7
#Problem address : https://projecteuler.net/problem=7
def isPrimeNumber(number):
    count=0
    for i in range(1,number+1):
        if number % i ==0:
            count+=1
        
    if count == 2:
        return True
    else:
        return False

def PrimeNumber10001st(number=10001):
    count=0
    primeNumber=1
    while count !=number:
        if isPrimeNumber(primeNumber):
            count+=1
        primeNumber+=1

    return primeNumber-1

print(PrimeNumber10001st(2))

