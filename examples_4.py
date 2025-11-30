#This code finds polindrome number made from the product two 3 digit number.
#problem address : https://projecteuler.net/problem=4
def isPalindrom(number):
    tempNumber=number
    reverseNumber=0
    while tempNumber!=0:
        reverseNumber=reverseNumber*10
        reverseNumber+=tempNumber%10
        tempNumber=tempNumber//10
    if number==reverseNumber: 
        return True
    else:
        return False
    
    
def find_Palindrom():
    polindrom=[]
    for i in range(100,1000):
        for j in range(i,1000):
            if isPalindrom(i*j):
                polindrom.append(i*j)

    return polindrom

print(find_Palindrom())
