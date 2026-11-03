#算术运算符（数学运算）：+-*/  // ** %
print(9%4) #1
print(8/4) #2.0 除法不管有没有小数输出都为小数
print(9//4) #2
print(2**2) #4
#赋值运算符:将=右侧赋值到左边
    #多变量赋值:变量顺序和数据顺序要对应
num,float,str1=1,2.2,'zhe'
print(num)
print(float)
print(str1)
    #多个变量赋相同值
a=b=10
print(a)
print(b)

#复合赋值运算符：c+=a相当于c=c+a以此类推,先进行算术运算符再赋值运算符
a=100
a+=1
print(a)
#注意：复杂情况先算右边算术表达式，再算复合赋值运算
c=10
c+=1+2
print(c)
d=10
d*=1+2
print(d)
#比较运算符:==(判断相等)  !=(不等于) > <  >=  <= 正确得到True 错误得到False
a=1
b=1
print(a==b)  #True

#逻辑运算符 
a=0
b=1
c=2
# and(与) x and y :都真才真 一假全假
print(a<b and c>b)#True
print(a>b and c>b)#False
# or(或) x or y : 一真则真 都假才假
print(a<b or c>b)
print(a>b or c>b) #True
# not(非)：取反义
print(not False) #True
print(not c>b) #False
