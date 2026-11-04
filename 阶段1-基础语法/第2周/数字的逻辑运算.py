a=0
b=1
c=2
# and运算符，只要一个值为0则结果为0，否则结果为(最后一个)非0数字
print(a and b) #0
print(b and a) #0
print(b and c) #2
print(c and b) #1
# or运算符，只有所有值为0结果才为0，否则结果为(第一个)非0数字
print(a or b) #1
print(a or c) #2
print(b or c) #1
