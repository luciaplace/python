''' 이중 반복문
    for 변수1 in range(시작, 끝, 증가):
        for 변수2 in range(시작, 끝, 증가):
            반복할 문장 '''

#1 구구단
for dan in range(2,10,1):
    for val in range(1,10):
        print("%d * %d = %d" %(dan,val, dan*val))
    print()

#2 별찍기
star ="*"
for col in range(1,6):
    for row in range(0,col):
        print(star, end="")
    print()