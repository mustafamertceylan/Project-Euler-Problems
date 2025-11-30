#This code calculate sum of multiples of the fibonacci squence terms...
#problem address: https://projecteuler.net/problem=2
def sum_of_fibonacci(upperLimit=4000000):
    fibonacci_list=[1,2]
    sum=fibonacci_list[0]+fibonacci_list[1]
    i=0
    while sum<=upperLimit:
        fibonacci_list.append(fibonacci_list[i]+fibonacci_list[i+1])
        sum+=fibonacci_list[-1]
        i+=1
    print(sum)
    
sum_of_fibonacci(100)