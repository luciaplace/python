''' break : 반복문 안에서 break 가 있는 경우 반복문을 빠져나온다. '''

#1
a=0
while True :
    if a>100:
        break
    print('a의 값은 :',a)
    a+=1
print('a는 100보다 크다')


'''continue : 반복문 안에서 특정 조건만족시에 도달하며, continue 이하의 수행은 무시하고 다시 반복의 시작점인 
    while 문으로 이동하여 그다음의 수행을 한다. '''

#1
a=0
while a<100:
    a += 1
    if a>80 and a<90 :
        continue
    print('a의 값은 :',a)