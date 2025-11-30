#ProjectEuler problem 5
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#Problem address : https://projecteuler.net/problem=6
def SumSquareDifference(number):
    SquareOfSum=0
    for i in range(number+1):
        SquareOfSum+=i
    SumOfSquare=SumOfSquare**2

    SumOfSquare=0
    for i in range(number+1):
        SumOfSquare+=i**2
    return abs(SumOfSquare-SquareOfSum)

print(SumSquareDifference(10))