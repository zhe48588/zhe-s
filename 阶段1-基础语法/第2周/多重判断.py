age = int(input('年龄为:'))
if age < 18 :
    print('童工，不合法')
elif 18<= age <=60 :
    print('合法工龄')
else :      #else后面不能写条件
    print('法定退休年龄')
