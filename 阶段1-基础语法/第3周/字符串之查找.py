'''find语法:字符串序列.find(子串,开始位置下标,结束位置下标)#开始和结束位置下标可以忽略
   index语法:字符串序列.find(子串,开始位置下标,结束位置下标)
find()检测某个子串是否包含在这个字符串中，在返回子串开始位置下标，不在则返回-1
index()检测某个子串是否包含在这个字符串中，在返回子串开始位置下标，否则报错
count返回某个子串在字符串中出现的次数
'''
str1='hello world and itcast and itheima and Python'
print(str1.find('and')) #12
print(str1.find('and',15,30)) #23
print(str1.find('ands')) #-1
#find和index用法一样
#print(str1.index('ands')) #报错

#count统计次数
print(str1.count('and')) #3
print(str1.count('ands')) #0

#rfind rindex用法与find index一样，但是从右侧开始查找
print(str1.rfind('and'))