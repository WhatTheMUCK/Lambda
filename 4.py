print('Введите количество элементов массива')
n=int(input())
m=[]
if n%10<5 and n%10>0 and n//10!=1:
    print('Введите числа в массив',n,'раза')
if n%10>=5 or n%10==0 or n//10==1:
    print('Введите числа в массив',n,'раз')
for i in range(0,n):
    a=int(input())
    m=m+[a]
print('Если хотите узнать кол-во нулевых элементов в массиве, то напишите zero(m)')
def zero(m):
    k=0
    for i in range(0,len(m)):
        if m[i]==0:
            k=k+1
    return k
