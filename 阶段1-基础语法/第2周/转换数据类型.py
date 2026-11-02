#1.输入
num=input('输入一个数字:')
print(num)
#2.检验数据类型
print(type(num))  #str
#3.转换数据类型
int(num)
#4.检验数据类型
print(type(int(num)))


####转换数据类型的函数
#int(x)整数 float(x)浮点型 str(x)字符串 

#tuple(s)将序列s转换为元组 list(s)将序列转换为列表
list1=[10,20,30]
print(type(tuple(list1)))  #tuple
print(tuple(list1))#(10,20,30)

tuple1=(100,200,300)
print(type(list(tuple1)))  #list
print(list(tuple1))  #[100,200,300]

#eval(str)用来计算在字符串中有效python表达式，并返回一个值
#人话:把字符串里面的数据转换为原本的数据
str1='1'
str2='1.1'
str3='[1,2,3]'
str4='(4,5,6)'
print(eval(str1))  #1
print(eval(str2))  #1.1
print(eval(str3))  #[1,2,3]
print(eval(str4))  #(4,5,6)