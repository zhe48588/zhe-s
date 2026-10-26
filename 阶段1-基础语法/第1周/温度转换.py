#input()输入 print()输出
#成员运算符in
#eval函数 if-elif-else format()格式化输出
T = input("请输入带符号的温度值:")
if T[-1] in['C','c']:
    F=float(T[0:-1])*1.8+32
    print("换算后的温度为{:.2f}F".format(F))
elif T[-1] in['F','f']:
    C=(float(T[0:-1])-32)/1.8
    print("换算后的温度为{:.2f}C".format(C))
else:
    print("格式错误")


