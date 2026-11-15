"""
break终止循环(当某些条件成立.退出整个循环)
continue退出当前循环.执行下一个循环
"""
#循环吃5个苹果，吃完第3个吃饱了，第4和5不吃了
i = 1
while i<=5:
    if i==4:
        print('吃饱了')
        break
    print(f'吃了{i}个苹果')
    i+=1
#i+=1和if语句是平级关系 都属于while循环



#
i = 1
while i<= 5:
    if i==3:
        print('有虫子不吃了')
        i+=1
        #若要使用continue 必须在continue之前修改计数器 否则进入死循环
        continue
    print(f'吃第{i}个苹果')
    i+=1

