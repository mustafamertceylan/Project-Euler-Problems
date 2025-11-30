# This code finds the prime factors of given number.
# problem address : https://projecteuler.net/problem=3
def prime_factors(number):
    prime_factorsList=[]
    for i in range(2,(number//2)+1):
        if number%i==0 and prime_factors(i)==i:
            prime_factorsList.append(i)

    if len(prime_factorsList)==0:
        return number 
    return prime_factorsList
        
    
print(prime_factors(600851475143))