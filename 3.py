m=[]
print('Введите 10 чисел массива')
for i in range(0,10):
    a=int(input())
    m=m+[a]
print('Для того, чтобы посчитать сумму элементов массива введите: Sum(m)')
def Sum(m):
    return sum(m)
