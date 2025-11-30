#ProjectEuler problem 5
#problem address : https://projecteuler.net/problem=5
#That code calculates the least common multiple of all numbers between 1 to 20
def isPrimeNumber(number):
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count+=1
    if count==2:
        return True
    else: return False

def LCM(number):#Least common multiple
    list=[]
    for i in range(2,number+1):
        if isPrimeNumber(i):
            list.append(i)
    newlist=[]
    for i in list:
        count=1
        while i**count<=number:
            count+=1
        newlist.append(i**(count-1))
    result=1
    for i in newlist:
        result*=i
    return result
 
print(LCM(20))


