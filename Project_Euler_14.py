list = ["number of iteration ", 0, "number ", 0]
for i in range(1,10**6):
    number = i
    count = 0
    while(number != 1):
        if number % 2 == 0:
            number=number / 2
            count+=1
        else:
            number = number*3 +1
            count+=1
    if (list[1]<count):
        list[1]=count
        list[3]=i

print(list)

