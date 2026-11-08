#语法：  条件成立执行的表达式 if 条件 else 条件不成立执行的表达式 
a = 1
b = 2
c = a if a > b else b  #意思是如果a大于b则给c赋值a，否则赋值b
print(c)
#有两个变量z m比较大小 如果z大于m 执行 z-m；负责m-z
z = int(input('输入：'))
m = int(input('输入：'))
l = (z-m) if z>m else (m-z)
print(l)
