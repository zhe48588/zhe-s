#打印星星一行五个 一共五行
j = 0
while j<5:
    i = 0
    while i<5:
        print('*',end='')
        i+=1
    print()#使用空print实现换行
    j+=1