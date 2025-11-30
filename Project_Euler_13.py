import random
list=[1]*100
for i in range(100):
    list[i]=random.randint(10000000000000000000000000000000000000000000000000,99999999999999999999999999999999999999999999999999)

print(list)

copyList=list.copy()
sum = 0

for i in range(40):
    for j in range(100):
        sum += copyList[j] % 10
        copyList[j] = copyList[j] // 10
    sum = sum // 10 

for i in range( 100 ):
    sum += copyList[i]

print("---------------------")

print(sum)

