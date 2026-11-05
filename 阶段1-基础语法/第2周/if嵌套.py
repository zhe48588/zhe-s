"""
if 条件1:
    条件1成立执行的代码
    if 条件2:
        条件2成立执行的代码
"""
#判断能否上车：有钱可以上车，没有钱不能上车 如果上车了，判断能不能坐下
money = float(input('输入你有多少钱:'))

if money >= 1.0:
    print('可以上车')
    seat = int(input('车上还有多少座位:'))
    if seat >= 1:
        print('有座位可以坐')
    else :
        print('站着吧')
else:
    print('上不了车')

    


