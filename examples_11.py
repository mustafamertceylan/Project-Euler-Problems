import random
#20*20 lik bir matris oluşturdum
matris = [[0 for i in range(20)] for j in range(20) ]
#20*20lik bir matris oluşturduk ardından içerisin 1 den 100 e kadar rastgele sayılarla doldurduk
for i in range(20):
    for j in range(20):
        matris[i][j]=random.randint(1,100)
    

#matrisi ekrana bastırdırk
for i in range(20):
    for j in range(20):
        print(matris[i][j],sep=" ",end="-- ")
    print("")

#ilk olarak matristeki yatayda bulunan en büyük 4 elemanı bulan fonksiyonu yazalım

def VerticalMax(matris):
    max=1
    temp=1
    elemanlar=[0]*4
    for i in range(20):
        for j in range(17):
            temp=matris[j][i]*matris[j+1][i]*matris[j+2][i]*matris[j+3][i]
            if(max<=temp):
                max=temp
                elemanlar=[matris[j][i],matris[j+1][i],matris[j+2][i],matris[j+3][i]]
            temp=1

    print(f"max çarpım {max} max elemanlar {elemanlar}")
    return max
        
def HorizontalMax(matris):
    max=1
    temp=1
    elemanlar=[]
    for i in range(20):
        for j in range(17):
            temp=matris[i][j]*matris[i][j+1]*matris[i][j+2]*matris[i][j+3]
            if max<=temp:
                max=temp
                elemanlar=[matris[i][j],matris[i][j+1],matris[i][j+2],matris[i][j+3]]
    print(f"max horizontal multiplex {max} and elements of the result {elemanlar}" )
    return max



def MaxDiagonalMultiplication(matris):
        temp = 1
        max= 1
        list=[]
        count=1
        for i in range(20):
            for j  in range(20):
                if i-4 > 0 and j+4 < 20 : 
                    temp = matris[i][j]*matris[i-1][j+1]*matris[i-2][j+2]*matris[i-3][j+3]
                    if temp>= max : 
                        max = temp
                        list = [matris[i][j],matris[i-1][j+1],matris[i-2][j+2],matris[i-3][j+3] , " indisler " , i ,j ]

        print(max, "  " ,list )
        return max

def MaxDiagonalLeft(matris):
    temp=1
    max=1
    list=[]
    for i in range(20):
        for j in range(20):
            if i+4 <20 and j+4 < 20 :
                temp=matris[i][j]*matris[i+1][j+1]*matris[i+2][j+2]*matris[i+3][j+3]
                if max<= temp:
                    max=temp
                    list=[matris[i][j],matris[i+1][j+1],matris[i+2][j+2],matris[i+3][j+3],"start of index : ", i,j]
    print(f" max : {max} {list}")
    return max


Left_Diagonal_multiplication=MaxDiagonalLeft(matris)
Right_Dioganal_Multiplication=MaxDiagonalMultiplication(matris)
Horizantal=HorizontalMax(matris)
Vertical=VerticalMax(matris)

print(f"Max multiplication {max(Left_Diagonal_multiplication,Right_Dioganal_Multiplication,Horizantal,Vertical)}")

