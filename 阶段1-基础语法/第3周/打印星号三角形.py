#一行输出星星个数与行数相同
i=0
while i<5:
    j=0
    while j<=i:
        print('*',end='')
        j+=1
    print()
    i+=1
#由内层循环控制*的个数，外层循环控制行数