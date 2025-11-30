import math
def number_of_divisor_count(number , divisorlist = False):
    count=0
    list=[]
    for i in range(1,int(math.sqrt(number))):
        if number % i == 0 : 
            count+=1
            list.append(i)
    if divisorlist:
        print(list) 
    return count

count = 1

divisor_count=0
number1=0

while divisor_count<=500:
    number1=(count*(count+1))//2
    divisor_count=number_of_divisor_count(number1)
    count+=1

print(number_of_divisor_count(number1,True))