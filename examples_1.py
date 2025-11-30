#The codes that finds sum of multiples of 3 or 5 below 1000
#The problem adress : https://projecteuler.net/problem=1
sum=0
i=1
while i<=1000:
    if i%3==0 or i%5==0:
        sum+=i
    i+=1
print(sum)