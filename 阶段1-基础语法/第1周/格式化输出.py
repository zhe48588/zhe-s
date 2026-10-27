name='zhe';age=19;weight=55.5;stu_id=1;
#字符串类型用%s
print('我的名字是%s'%name)
#带符号的整数用%d
print('年龄为%d岁'%age)
#浮点型用%f
print('体重为%.2f公斤'%weight)###小数点后要几位就.几f
print('学号为%d'%stu_id)
#学号为001时
print('学号为%03d'%stu_id)###想要几位数就写0几，位数本来就够则正常显示
#姓名，年龄，体重一块输出
print('我的名字是%s,年龄是%d,体重是%.2f'%(name,age,weight))
###多个变量要用小括号括起来，并用,隔开
#明年我的年龄
print('我的名字是%s,明年年龄是%d'%(name,age + 1))
