import random 
gamer = int(input('请出拳0--石头;1--剪刀;2--布:'))
computer = random.randint(0,2)
print(computer) #查看电脑出啥了
if (gamer==0 and computer==1)or(gamer==1 and computer==2)or(gamer==2 and computer==0):
    print('gamer win')
elif (gamer==1 and computer==0)or(gamer==2 and computer==1)or(gamer==0 and computer==2):
    print('computer win')
else :
    print('平局')