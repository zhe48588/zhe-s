'''字符串.replace(旧子串,新子串,替换次数)
替换次数不写代表全部替换
替换次数超出子串出现次数表示替换全部
'''
str1='hello world and itcast and itheima and Python'
print(str1.replace('and','he'))
'''
split()--分割,返回列表
字符串序列.split(分割字符,num)
num表示分割字符出现的次数，即将来返回数据个数为num+1个
'''
list1 = str1.split('and')
print(list1)
""" 
字符或子串.join()
join()--合并列表里面的字符串数据为一个大字符串
"""
zhe1 = ['11','22','33']
zhe2 = 'and'.join(zhe1)
print(zhe2)