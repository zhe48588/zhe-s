"""语法
for 临时变量 in 序列:
    重复执行的代码1
    ...代码2

"""
str1 = 'itheima'
for i in str1:
    print(i)

#break退出for循环
str1 = 'itheima'
for i in str1:
    if i=='e':
        print('遇到e不打印')
        break
    print(i)



#continue
str1 = 'itheima'
for i in str1:
    if i=='m':
        continue
    print(i)